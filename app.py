from flask import Flask, jsonify, request
from flask_cors import CORS  # allow frontend JS to call this API

app = Flask(__name__)
CORS(app)  # enable CORS for all routes (fine for this project)


@app.route("/")
def home():
    return """
    <h1>travelSmart Flask backend is running</h1>
    <p>Available endpoints (click one):</p>
    <ul>
        <li><a href="/api/places">Places (HTML)</a></li>
        <li><a href="/api/foods">All foods (JSON)</a></li>
        <li><a href="/api/hotels">Hotels (HTML)</a></li>
        <li><a href="/api/recommend-summary">Recommend food + place (JSON)</a></li>
    </ul>
    """


# -------------------- DATA --------------------

# Main attractions in Manhattan and Brooklyn
places = [
    {
        "name": "Central Park",
        "borough": "Manhattan",
        "description": "Large urban park with walking paths, lakes, and open fields.",
        "location": "Manhattan, NYC"
    },
    {
        "name": "Times Square",
        "borough": "Manhattan",
        "description": "Bright lights, Broadway shows, and a busy commercial district.",
        "location": "Midtown Manhattan, NYC"
    },
    {
        "name": "Brooklyn Bridge Park",
        "borough": "Brooklyn",
        "description": "Waterfront park with skyline views and walking paths along the East River.",
        "location": "DUMBO / Brooklyn Heights, Brooklyn, NYC"
    },
    {
        "name": "Prospect Park",
        "borough": "Brooklyn",
        "description": "Major Brooklyn park with meadows, a lake, and wooded trails.",
        "location": "Prospect Park, Brooklyn, NYC"
    }
]

# Quick lookup by place name
place_by_name = {p["name"]: p for p in places}

# Food spots, each linked to a nearby attraction
foods = [
    {
        "name": "Katz's Delicatessen",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Jewish Deli",
        "description": "Iconic deli famous for pastrami sandwiches and classic Lower East Side vibes.",
        "location": "Lower East Side, Manhattan",
        "website": "https://katzsdelicatessen.com/",
        "nearby_place_name": "Times Square"
    },
    {
        "name": "Joe's Pizza",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Pizza",
        "description": "Classic New York–style pizza slices with a thin, crispy crust.",
        "location": "Greenwich Village, Manhattan",
        "website": "https://www.joespizzanyc.com/",
        "nearby_place_name": "Central Park"
    },
    {
        "name": "Levain Bakery",
        "borough": "Manhattan",
        "type": "Bakery",
        "cuisine": "Bakery / Dessert",
        "description": "Famous bakery known for giant cookies and fresh baked goods.",
        "location": "Upper West Side, Manhattan",
        "website": "https://levainbakery.com/",
        "nearby_place_name": "Central Park"
    },
    {
        "name": "Juliana's Pizza",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Pizza / Italian",
        "description": "Coal‑fired pizzeria near the Brooklyn waterfront.",
        "location": "DUMBO, Brooklyn",
        "website": "https://www.julianaspizza.com/",
        "nearby_place_name": "Brooklyn Bridge Park"
    },
    {
        "name": "Oxomoco",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Mexican",
        "description": "Wood‑fired Mexican restaurant in Greenpoint.",
        "location": "Greenpoint, Brooklyn",
        "website": "https://oxomoconyc.com/",
        "nearby_place_name": "Brooklyn Bridge Park"
    },
    {
        "name": "Di Fara Pizza",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Pizza / Italian-American",
        "description": "Legendary pizzeria famous for hand‑crafted pies.",
        "location": "Midwood, Brooklyn",
        "website": "http://www.difarapizzany.com/",
        "nearby_place_name": "Prospect Park"
    }
]

# Example hotels (not used by the popup but kept for completeness)
hotels = [
    {
        "name": "Manhattan Hotel",
        "borough": "Manhattan",
        "stars": 4,
        "price_range": "$$$",
        "description": "Example hotel located in Midtown Manhattan.",
        "location": "Midtown, Manhattan",
        "website": "https://example-manhattan-hotel.com/"
    },
    {
        "name": "Brooklyn Boutique Hotel",
        "borough": "Brooklyn",
        "stars": 3,
        "price_range": "$$",
        "description": "Example boutique hotel in Brooklyn.",
        "location": "Williamsburg, Brooklyn",
        "website": "https://example-brooklyn-hotel.com/"
    }
]


# -------------------- BASIC ENDPOINTS --------------------

@app.route("/api/places", methods=["GET"])
def get_places():
    """Simple HTML page listing places with quick links."""
    html = """
    <h2>Places</h2>
    <ul>
    """
    for p in places:
        name = p["name"]
        borough = p["borough"]
        html += f"""
        <li>
          {name} ({borough})
          - <a href="/api/foods?borough={borough}">Food in {borough}</a>
          - <a href="/api/hotels-data?borough={borough}">Hotels in {borough}</a>
        </li>
        """
    html += """
    </ul>
    <p><a href="/">Back home</a></p>
    """
    return html


@app.route("/api/foods", methods=["GET"])
def get_foods():
    """Return all foods, or filter by borough with ?borough=Manhattan."""
    borough = request.args.get("borough")
    if borough:
        filtered = [f for f in foods if f["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(foods)


# -------------------- SURVEYS --------------------

surveys = []  # in‑memory storage


@app.route("/api/surveys", methods=["POST"])
def save_survey():
    """Receive a survey from the frontend and store it in memory."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON provided"}), 400
    surveys.append(data)
    return jsonify({"status": "ok", "count": len(surveys)})


# -------------------- RECOMMENDATION ("AI") --------------------

@app.route("/api/recommend-summary", methods=["GET"])
def recommend_summary():
    """
    Use the most recent survey to recommend:
    - one food place (based on cuisine + borough),
    - one nearby attraction for that food.
    Returns JSON: {"food": {...}, "place": {...}}.
    """
    if not surveys:
        return jsonify({"error": "no-surveys"}), 400

    last = surveys[-1]

    # These keys must match your survey form field names
    pref_cuisine = (last.get("cuisine") or "").lower()       # free‑text cuisine
    distance = last.get("distance")                          # "Within 30 minutes", "Within 1 hour", etc.

    # Simple rule to infer borough from distance answer
    if distance == "Within 30 minutes":
        preferred_borough = "Manhattan"
    elif distance == "Within 1 hour":
        preferred_borough = "Brooklyn"
    else:
        preferred_borough = "Manhattan"

    # 1) Choose a food: try cuisine + borough, then fallbacks
    chosen_food = None

    # cuisine + borough match
    if pref_cuisine:
        for f in foods:
            if preferred_borough and f["borough"].lower() != preferred_borough.lower():
                continue
            if pref_cuisine in f["cuisine"].lower():
                chosen_food = f
                break

    # just borough match
    if chosen_food is None:
        for f in foods:
            if f["borough"].lower() == preferred_borough.lower():
                chosen_food = f
                break

    # any food
    if chosen_food is None and foods:
        chosen_food = foods[0]

    # 2) Find the nearby place for that food
    chosen_place = None
    if chosen_food:
        nearby_name = chosen_food.get("nearby_place_name")
        if nearby_name and nearby_name in place_by_name:
            chosen_place = place_by_name[nearby_name]

    # fallback: any place in same borough
    if chosen_place is None and chosen_food:
        for p in places:
            if p["borough"].lower() == chosen_food["borough"].lower():
                chosen_place = p
                break

    if chosen_place is None and places:
        chosen_place = places[0]

    return jsonify({
        "food": chosen_food,
        "place": chosen_place
    })


# -------------------- HOTELS (optional) --------------------

@app.route("/api/hotels-data", methods=["GET"])
def hotels_data():
    borough = request.args.get("borough")
    if borough:
        filtered = [h for h in hotels if h["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(hotels)


@app.route("/api/hotels", methods=["GET"])
def hotels_page():
    return """
    <h2>Hotels</h2>
    <p>Choose a borough:</p>
    <ul>
        <li><a href="/api/hotels-data?borough=Manhattan">Manhattan hotels</a></li>
        <li><a href="/api/hotels-data?borough=Brooklyn">Brooklyn hotels</a></li>
    </ul>
    <p><a href="/">Back home</a></p>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
