# api_gateway/gateway.py

from flask import Flask, request, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
from api_gateway.config import SERVERS, TIMEOUT
from api_gateway.utils import ServerStatus

app = Flask(__name__)
server_status = ServerStatus(SERVERS)  # Initialize server tracker

def forward_request(server, data):
    """
    Forward request to an available backend server.
    """
    try:
        response = requests.post(server, json=data, timeout=TIMEOUT)
        return response.json()
    except requests.exceptions.RequestException:
        return {"error": f"Server {server} is unreachable."}
    finally:
        server_status.mark_idle(server)  # Mark server as idle

@app.route("/process", methods=["POST"])
def handle_request():
    """
    Handle incoming requests and distribute them to idle servers.
    """
    data = request.json
    idle_server = server_status.get_idle_server()

    if not idle_server:
        return jsonify({"error": "All servers are busy. Try again later."}), 503

    with ThreadPoolExecutor() as executor:
        future = executor.submit(forward_request, idle_server, data)
        result = future.result()

    return jsonify(result)

def run_gateway():
    """
    Start the Flask API Gateway.
    """
    app.run(port=5000, debug=True)
