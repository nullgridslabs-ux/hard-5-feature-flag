# hard-5-feature-flag/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>AI Query Gateway</h2>
<p>Unified AI access layer for internal and enterprise users.</p>
<ul>
<li>POST /api/ai/query</li>
<li>GET /health</li>
</ul>
<p>Some features are restricted to enterprise customers.</p>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/api/ai/query", methods=["POST"])
def ai():
    data = request.json or {}

    if data.get("features", {}).get("enterprise_ai"):
        return jsonify({"answer":"beta result","flag":FLAG})

    return jsonify({"error":"feature disabled"}),403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
