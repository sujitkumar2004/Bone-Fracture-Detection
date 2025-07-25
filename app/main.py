

from flask import Flask, request, jsonify, redirect
from app import get_store
from app.utils import generate_short_code, is_valid_url
from datetime import datetime

app = Flask(__name__)

@app.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing URL"}), 400

    long_url = data["url"]
    if not is_valid_url(long_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    store = get_store()

    while short_code in store:
        short_code = generate_short_code()

    store[short_code] = {
        "original_url": long_url,
        "created_at": datetime.now().isoformat(),
        "clicks": 0
    }

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    })

@app.route("/<short_code>", methods=["GET"])
def redirect_to_original(short_code):
    store = get_store()
    if short_code not in store:
        return jsonify({"error": "Not found"}), 404

    store[short_code]["clicks"] += 1
    return redirect(store[short_code]["original_url"])

@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    store = get_store()
    if short_code not in store:
        return jsonify({"error": "Not found"}), 404

    entry = store[short_code]
    return jsonify({
        "url": entry["original_url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"]
    })

if __name__ == "__main__":
    app.run(debug=True)
