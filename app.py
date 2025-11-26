from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data: NYC places by borough
places = [
    {"name": "Central Park", "borough": "Manhattan", "type": "Outdoor"},
    {"name": "Brooklyn Museum", "borough": "Brooklyn", "type": "Museum"},
    {"name": "Yankee Stadium", "borough": "Bronx", "type": "Sports"},
    {"name": "Flushing Meadows", "borough": "Queens", "type": "Outdoor"},
    {"name": "Snug Harbor", "borough": "Staten Island", "type": "Garden"},
]

@app.route("/api/places", methods=["GET"])
def get_places():
    borough = request.args.get("borough")
    if borough:
        filtered = [p for p in places if p["borough"].lower() == borough.lower()]
        return jsonify(filtered)
    return jsonify(places)

if __name__ == "__main__":
    app.run(port=5000)
