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
        <li><a href="/api/places">Places</a></li>
        <li><a href="/api/foods">All foods</a></li>
        <li><a href="/api/surveys">Surveys</a></li>
        <li><a href="/api/recommend-places">Recommendations</a></li>
        <li><a href="/api/hotels">All hotels</a></li>
    </ul>
    """



# Places data
places = [
    {"name": "Central Park", 
     "borough": "Manhattan"
    },
    {"name": "Brooklyn Bridge Park", 
     "borough": "Brooklyn"
    },
]

# Foods data
foods = [
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
    },  
    {
        "name": "Katz's Delicatessen",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Jewish / Deli",
        "description": "Historic kosher-style delicatessen known for its massive pastrami (and corned beef) sandwiches — a New York classic.",
        "location": "205 East Houston Street, Lower East Side, Manhattan, NY 10002",
        "website": ""
    },
    {
        "name": "Marea",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Italian / Seafood",
        "description": "Upscale Italian and seafood restaurant near Columbus Circle — recognized as one of the city's top Italian-seafood spots.",
        "location": "240 Central Park South, Manhattan, NY 10019",
        "website": ""
    },
    {
        "name": "Jean-Georges",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "French / New American",
        "description": "Flagship restaurant mixing French and New American cuisine, with seasonal menus and high-end dining near Central Park.",
        "location": "1 Central Park West (at Columbus Circle), Manhattan, NY",
        "website": ""
    },
    {
        "name": "Gramercy Tavern",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "New American",
        "description": "Beloved farm-to-table New American tavern and dining room, known for its warm hospitality and seasonal dishes.",
        "location": "Flatiron/Gramercy area, Manhattan, NY",
        "website": ""
    },
    {
        "name": "César",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Seafood / Contemporary",
        "description": "Michelin-starred seafood restaurant opened in 2024, offering refined seafood-forward dishes in Hudson Square.",
        "location": "333 Hudson Street, Hudson Square, Manhattan, NY 10013",
        "website": "https://www.cesar.restaurant/"
    },
    {
        "name": "Lucali",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Italian / Pizza",
        "description": "Beloved brick-oven pizzeria in Carroll Gardens, known for its Neapolitan-style pies and calzones — often listed among NYC’s best pizza spots.",
        "location": "575 Henry St, Carroll Gardens, Brooklyn, NY 11231",
        "website": "https://www.lucali.com/"
    },
    {
        "name": "Di Fara Pizza",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Pizza / Italian-American",
        "description": "Legendary pizzeria in Midwood — frequently called one of the best pizza spots in NYC, famous for its classic handmade pies and decades-old tradition.",
        "location": "1424 Avenue J, Midwood, Brooklyn, NY 11230",
        "website": "http://www.difarapizzany.com/"
    },
    {
        "name": "L&B Spumoni Gardens",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Italian-American / Sicilian Pizza",
        "description": "Historic Italian-American pizzeria and restaurant (est. 1939), famous for its Sicilian square-slice pizza and classic spumoni desserts.",
        "location": "2725 86th Street, Gravesend, Brooklyn, NY 11223",
        "website": "https://spumonigardens.com/"
    },
    {
        "name": "Randazzo's Clam Bar",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Seafood / Italian-American",
        "description": "Old-school seafood institution in Sheepshead Bay (opened 1963), known for generous portions, clam dishes, lobster fra diavolo, and longtime loyal customers.",
        "location": "2017 Emmons Avenue, Sheepshead Bay, Brooklyn, NY 11235",
        "website": "http://randazzosclambar.nyc/"
    },
    {
        "name": "Oxomoco",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Mexican",
        "description": "Wood-fired Mexican restaurant in Greenpoint — Michelin-starred, celebrated for inventive tacos and wood-grilled dishes, blending traditional flavors with modern technique.",
        "location": "128 Greenpoint Avenue, Greenpoint, Brooklyn, NY 11222",
        "website": "https://oxomoconyc.com/"
    },
    {
        "name": "A&A Bake and Doubles Shop",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Trinidadian / Caribbean",
        "description": "Bed-Stuy restaurant serving Trinidad and Tobago–style doubles, aloo pies and other Caribbean comfort food — praised for authenticity and vibrant flavors.",
        "location": "Bed-Stuy, Brooklyn, NY",
        "website": ""
    }
]

# Hotel data
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

@app.route("/api/places", methods=["GET"])
def get_places():
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
          - <a href="/api/foods?borough={borough}">food in {borough}</a>
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

# data for hotels (filter by borough)
@app.route("/api/hotels-data", methods=["GET"])
def hotels_data():
    borough = request.args.get("borough")
    if borough:
        filtered = [h for h in hotels if h["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(hotels)


# HTML page listing hotels and links
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
