# hard-5-feature-flag/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/api/ai/query", methods=["POST"])
def ai():
    data = request.json or {}

    # BUG: client controls feature flag
    if data.get("features", {}).get("enterprise_ai"):
        return jsonify({"answer":"beta result","flag":FLAG})

    return jsonify({"error":"feature disabled"}),403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
