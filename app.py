from flask import Flask, jsonify, request

app = Flask(__name__)

# ADD THIS ROUTE so / works
@app.route("/")
def home():
    return "<h1>travelSmart Flask backend is running</h1><p>Try /api/places</p>"

# Example NYC places data
places = [
    {"name": "Central Park", "borough": "Manhattan", "type": "Outdoor"},
    {"name": "Brooklyn Museum", "borough": "Brooklyn", "type": "Museum"},
    {"name": "Yankee Stadium", "borough": "Bronx", "type": "Sports"},
    {"name": "Flushing Meadows–Corona Park", "borough": "Queens", "type": "Outdoor"},
    {"name": "Snug Harbor Cultural Center", "borough": "Staten Island", "type": "Garden"},
]

@app.route("/api/places", methods=["GET"])
def get_places():
    borough = request.args.get("borough")
    if borough:
        filtered = [p for p in places if p["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(places)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
