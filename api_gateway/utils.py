# api_gateway/utils.py

import threading

class ServerStatus:
    def __init__(self, servers):
        self.lock = threading.Lock()
        self.status = {server: True for server in servers}  # True = idle, False = busy

    def get_idle_server(self):
        with self.lock:
            for server, is_idle in self.status.items():
                if is_idle:
                    self.status[server] = False  # Mark as busy
                    return server
        return None  # No idle server

    def mark_idle(self, server):
        with self.lock:
            self.status[server] = True
