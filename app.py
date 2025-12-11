from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:3000"}})


@app.route("/")
def home():
    return """
    <h1>travelSmart Flask backend is running</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/api/places">/api/places</a></li>
        <li><a href="/api/foods">/api/foods</a></li>
        <li><a href="/api/surveys">POST /api/surveys</a></li>
        <li><a href="/api/recommend-places">/api/recommend-places</a></li>
        <li><a href="/api/recommend-foods">/api/recommend-foods</a></li>
        <li><a href="/api/recommend-summary">/api/recommend-summary</a></li>
    </ul>
    """


# ---------- DATA ----------

places = [
    {
        "name": "Central Park",
        "borough": "Manhattan",
        "description": "Large urban park with walking paths, lakes, and open fields.",
        "location": "Manhattan, NYC",
        "website": "https://www.centralparknyc.org/",
        "type": "Outdoor",
    },
    {
        "name": "The Museum of Modern Art",
        "borough": "Manhattan",
        "description": "Works from van Gogh to Warhol & beyond plus a sculpture garden, 2 cafes & The Modern restaurant.",
        "location": "Manhattan, NYC",
        "website": "https://www.moma.org/",
        "type": "Museums",
    },
    {
        "name": "Empire State Building",
        "borough": "Manhattan",
        "description": "Iconic, art deco office tower from 1931 with exhibits & observatories on the 86th & 102nd floors.",
        "location": "Manhattan, NYC",
        "website": "https://www.esbnyc.com/",
        "type": "Landmarks",
    },

    {
        "name": "Brooklyn Bridge Park",
        "borough": "Brooklyn",
        "description":"This urban oasis features shaded picnic tables, hibachi-style BBQ grills & river views.",
        "location": "Brooklyn, NYC",
        "website": "https://www.brooklynbridgepark.org/",
        "type": "Outdoor",
    },
    {
        "name": "Brooklyn Museum",
        "borough": "Brooklyn",
        "description":"One of the largest and oldest art museums in the United States.",
        "location": "Brooklyn, NYC",
        "website": "https://www.brooklynmuseum.org/",
        "type": "Museums",
    },
    {
        "name": "Brooklyn Bridge",
        "borough": "Brooklyn",
        "description": "Beloved, circa-1883 landmark connecting Manhattan & Brooklyn via a unique stone-&-steel design.",
        "location": "Brooklyn, NYC",
        "website": "https://www.nyc.gov/html/dot/html/infrastructure/brooklyn-bridge.shtml",
        "type": "Landmarks",
    },

    {
        "name": "Flushing Meadows–Corona Park",
        "borough": "Queens",
        "description": "Historic park known for the Unisphere and wide open spaces.",
        "location": "Queens, NYC",
        "website": "https://www.nycgovparks.org/parks/flushing-meadows-corona-park",
        "type": "Outdoor",
    },
    {
        "name": "New York Hall of Science",
        "borough": "Queens",
        "description": "This former 1964 World's Fair pavilion now houses more than 450 interactive science & tech exhibits.",
        "location": "Queens, NYC",
        "website": "https://nysci.org/",
        "type": "Museums",
    },
    {
        "name": "Lewis H. Latimer House",
        "borough": "Queens",
        "description": "Historical house-turned-museum of a well-known African American inventor & electrical pioneer.",
        "location": "Queens, NYC",
        "website": "https://www.lewislatimerhouse.org/",
        "type": "Landmarks",
    },
]

foods = [
    {
        "name": "Katz's Delicatessen",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Jewish / Deli",
        "description": "Historic kosher-style delicatessen known for its massive pastrami sandwiches.",
        "location": "Lower East Side, Manhattan",
        "website": "https://katzsdelicatessen.com/",
    },
    {
        "name": "Joe's Pizza",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Pizza",
        "description": "Classic New York–style pizza slices with a thin, crispy crust.",
        "location": "Greenwich Village, Manhattan",
        "website": "https://www.joespizzanyc.com/",
    },
    {
        "name": "Levain Bakery",
        "borough": "Manhattan",
        "type": "Bakery",
        "cuisine": "Bakery",
        "description": "Famous bakery known for giant, gooey cookies and fresh baked goods.",
        "location": "Upper West Side, Manhattan",
        "website": "https://levainbakery.com/",
    },
    {
        "name": "Los Tacos No. 1",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Mexican",
        "description": "Popular spot for authentic, fast casual tacos and Mexican street food.",
        "location": "Chelsea Market, Manhattan",
        "website": "https://lostacosno1.com/",
    },
    {
        "name": "Xi’an Famous Foods",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Chinese",
        "description": "Casual eatery known for hand-pulled noodles and spicy Western Chinese dishes.",
        "location": "Multiple locations in Manhattan",
        "website": "https://www.xianfoods.com/",
    },
    {
        "name": "Marea",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Italian / Seafood",
        "description": "Upscale Italian and seafood restaurant near Columbus Circle.",
        "location": "240 Central Park South, Manhattan",
        "website": "",
    },
    {
        "name": "Jean-Georges",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "French / New American",
        "description": "Flagship restaurant mixing French and New American cuisine near Central Park.",
        "location": "1 Central Park West, Manhattan",
        "website": "https://www.jean-georges.com",
    },
    {
        "name": "Gramercy Tavern",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "New American",
        "description": "Beloved farm-to-table New American tavern known for seasonal dishes.",
        "location": "Flatiron / Gramercy, Manhattan",
        "website": "https://www.gramercytavern.com",
    },
    {
        "name": "César",
        "borough": "Manhattan",
        "type": "Restaurant",
        "cuisine": "Seafood / Contemporary",
        "description": "Seafood restaurant in Hudson Square with refined seafood-forward dishes.",
        "location": "Hudson Square, Manhattan",
        "website": "https://www.cesar.restaurant/",
    },
    {
        "name": "Lucali",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Italian / Pizza",
        "description": "Brick-oven pizzeria in Carroll Gardens known for Neapolitan-style pies.",
        "location": "Carroll Gardens, Brooklyn",
        "website": "https://www.lucali.com/",
    },
    {
        "name": "Di Fara Pizza",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Pizza / Italian-American",
        "description": "Legendary pizzeria in Midwood famous for classic handmade pies.",
        "location": "Midwood, Brooklyn",
        "website": "http://www.difarapizzany.com/",
    },
    {
        "name": "L&B Spumoni Gardens",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Italian-American / Sicilian Pizza",
        "description": "Historic pizzeria known for Sicilian square slices and spumoni desserts.",
        "location": "Gravesend, Brooklyn",
        "website": "https://spumonigardens.com/",
    },
    {
        "name": "Randazzo's Clam Bar",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Seafood / Italian-American",
        "description": "Seafood institution in Sheepshead Bay known for clam dishes and lobster.",
        "location": "Sheepshead Bay, Brooklyn",
        "website": "http://randazzosclambar.nyc/",
    },
    {
        "name": "Oxomoco",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Mexican",
        "description": "Wood-fired Mexican restaurant in Greenpoint, Michelin-starred.",
        "location": "Greenpoint, Brooklyn",
        "website": "https://oxomoconyc.com/",
    },
    {
        "name": "A&A Bake and Doubles Shop",
        "borough": "Brooklyn",
        "type": "Restaurant",
        "cuisine": "Trinidadian / Caribbean",
        "description": "Bed-Stuy spot for doubles, aloo pies, and Caribbean comfort food.",
        "location": "Bed-Stuy, Brooklyn",
        "website": "https://www.yelp.com/biz/a-and-a-bake-and-double-and-roti-shop-brooklyn-3",
    },
]
# In‑memory survey storage
surveys = []


# ---------- API ROUTES ----------

@app.route("/api/places", methods=["GET"])
def get_places():
    return jsonify(places)


@app.route("/api/foods", methods=["GET"])
def api_foods():
    borough = request.args.get("borough")
    if borough:
        filtered = [f for f in foods if f["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(foods)

@app.route("/api/surveys", methods=["POST"])
def save_survey():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    surveys.append(data)
    return jsonify({"status": "saved", "count": len(surveys)})


@app.route("/api/recommend-places", methods=["GET"])
def recommend_places():
    if not surveys:
        return jsonify(places)

    last = surveys[-1]
    preferred_attractions = last.get("attractions", "").lower()
    preferred_cuisine = last.get("cuisine", "").lower()

    attraction_match = [
        p for p in places
        if preferred_attractions in p["type"].lower()
    ]
    if attraction_match:
        return jsonify(attraction_match)

    cuisine_match = [
        f for f in foods
        if preferred_cuisine in f["cuisine"].lower()
    ]
    if cuisine_match:
        return jsonify(cuisine_match)

    return jsonify(places)


@app.route("/api/recommend-foods", methods=["GET"])
def recommend_foods():
    if not surveys:
        return jsonify(foods)

    last = surveys[-1]
    pref_cuisine = last.get("cuisine", "").lower()
    pref_budget = last.get("mealBudget", "")
    pref_style = last.get("diningStyle", "").lower()
    restrictions = last.get("restrictions", "").lower()

    results = foods

    if pref_cuisine:
        results = [f for f in results if pref_cuisine in f["cuisine"].lower()]

    if restrictions and restrictions != "none":
        results = [f for f in results if restrictions not in f["description"].lower()]

    return jsonify(results)


@app.route("/api/recommend-summary", methods=["GET"])
def recommend_summary():
    if not surveys:
        return jsonify({"error": "no-surveys"}), 400

    last = surveys[-1]
    preferred_attractions = last.get("attractions", "").lower()
    preferred_cuisine = last.get("cuisine", "").lower()

    place_candidates = [
        p for p in places
        if preferred_attractions and preferred_attractions in p["type"].lower()
    ]
    best_place = place_candidates[0] if place_candidates else places[0]

    food_candidates = [
        f for f in foods
        if preferred_cuisine and preferred_cuisine in f["cuisine"].lower()
    ]
    best_food = food_candidates[0] if food_candidates else foods[0]

    return jsonify({
        "food": best_food,
        "place": best_place
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
