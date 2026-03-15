from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running", 200

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "pong"}), 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("Webhook:", data)
    return jsonify({"status": "ok"}), 200
