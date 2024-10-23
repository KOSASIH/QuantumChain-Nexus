# src/core/node.py

from flask import Flask, request, jsonify
import requests
import json
import hashlib

class Node:
    def __init__(self, node_id, host='localhost', port=5000):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.peers = set()  # Set of peer nodes
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """Set up HTTP routes for the node."""
        @self.app.route('/register', methods=['POST'])
        def register_peer():
            peer = request.json.get('peer')
            if peer:
                self.peers.add(peer)
                return jsonify({"message": "Peer registered successfully."}), 200
            return jsonify({"message": "Invalid peer."}), 400

        @self.app.route('/peers', methods=['GET'])
        def get_peers():
            return jsonify(list(self.peers)), 200

        @self.app.route('/broadcast', methods=['POST'])
        def broadcast_message():
            message = request.json.get('message')
            if message:
                self.broadcast(message)
                return jsonify({"message": "Message broadcasted."}), 200
            return jsonify({"message": "Invalid message."}), 400

    def broadcast(self, message):
        """Broadcast a message to all peers."""
        for peer in self.peers:
            try:
                requests.post(f'http://{peer}/receive', json={'message': message})
            except requests.exceptions.RequestException as e:
                print(f"Error sending message to {peer}: {e}")

    def start(self):
        """Start the node's HTTP server."""
        self.app.run(host=self.host, port=self.port)

# Example usage
if __name__ == "__main__":
    node = Node(node_id="Node1")
    node.start()
