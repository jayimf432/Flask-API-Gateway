# backend/server.py

from flask import Flask, request, jsonify
import time
import sys

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_request():
    data = request.json
    time.sleep(3)  # Simulate processing time
    return jsonify({"message": "Processed successfully", "data": data})

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    app.run(port=port)
