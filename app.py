from flask import Flask, jsonify, request
from flask_cors import CORS  # allow frontend JS to call this API

app = Flask(__name__)
CORS(app)  # enable CORS for all routes (fine for this project)


@app.route("/")
def home():
    return "<h1>travelSmart Flask backend is running</h1><p>Try /api/places, /api/foods, or /api/recommend-places</p>"


# Top 5 food spots in Manhattan (used as both places and foods)
places = [
    {
        "name": "Katz's Delicatessen",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Jewish Deli",
        "description": "Iconic NYC deli famous for pastrami sandwiches and classic Lower East Side vibes.",
        "location": "Lower East Side, Manhattan",
        "website": "https://katzsdelicatessen.com/"
    },
    {
        "name": "Joe's Pizza",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Pizza",
        "description": "Classic New York–style pizza slices with a thin, crispy crust.",
        "location": "Greenwich Village, Manhattan",
        "website": "https://www.joespizzanyc.com/"
    },
    {
        "name": "Levain Bakery",
        "borough": "Manhattan",
        "type": "Bakery",
        "cuisine": "Bakery",
        "description": "Famous bakery known for giant, gooey cookies and fresh baked goods.",
        "location": "Upper West Side, Manhattan",
        "website": "https://levainbakery.com/"
    },
    {
        "name": "Los Tacos No. 1",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Mexican",
        "description": "Popular spot for authentic, fast casual tacos and Mexican street food.",
        "location": "Chelsea Market, Manhattan",
        "website": "https://lostacosno1.com/"
    },
    {
        "name": "Xi’an Famous Foods",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Chinese",
        "description": "Casual eatery known for hand-pulled noodles and spicy Western Chinese dishes.",
        "location": "Multiple locations in Manhattan",
        "website": "https://www.xianfoods.com/"
    }
]

# Foods share same data as places for this project
foods = places


@app.route("/api/places", methods=["GET"])
def get_places():
    """Return all places, or filter by borough with ?borough=Manhattan."""
    borough = request.args.get("borough")
    if borough:
        filtered = [p for p in places if p["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(places)


@app.route("/api/foods", methods=["GET"])
def get_foods():
    """Return all foods, or filter by borough with ?borough=Manhattan."""
    borough = request.args.get("borough")
    if borough:
        filtered = [f for f in foods if f["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(foods)


# In‑memory survey storage
surveys = []


@app.route("/api/surveys", methods=["POST"])
def save_survey():
    """Receive a survey from the frontend and store it in memory."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON provided"}), 400
    surveys.append(data)
    return jsonify({"status": "ok", "count": len(surveys)})


@app.route("/api/recommend-places", methods=["GET"])
def recommend_places():
    """
    Simple 'AI' endpoint:
    use the most recent survey's 'cuisine' or 'attractions' field to filter.
    """
    if not surveys:
        return jsonify(places)

    last = surveys[-1]
    preferred_cuisine = last.get("cuisine")
    preferred_type = last.get("attractions")

    # Try cuisine-based match first
    if preferred_cuisine:
        matched = [
            p for p in places
            if preferred_cuisine.lower() in p.get("cuisine", "").lower()
        ]
        if matched:
            return jsonify(matched)

    # Then type-based match (if you align attractions with type)
    if preferred_type:
        matched = [p for p in places if p["type"].lower() == preferred_type.lower()]
        if matched:
            return jsonify(matched)

    # Fallback: return all
    return jsonify(places)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
