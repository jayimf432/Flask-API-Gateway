# api_gateway/config.py

# List of backend servers
SERVERS = [
    "http://127.0.0.1:6000/process",
    "http://127.0.0.1:6001/process",
    "http://127.0.0.1:6002/process",
    "http://127.0.0.1:6003/process",
    "http://127.0.0.1:6004/process"
]

# Maximum timeout for backend response
TIMEOUT = 10