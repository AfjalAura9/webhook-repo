from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from config import MONGO_URI
from utils.formatter import format_event
import certifi

app = Flask(__name__)
client = MongoClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())
db = client["webhook_db"]
collection = db["events"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/webhook', methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event", "")
    payload = request.json

    if event_type == "push":
        event = {
            "author": payload["pusher"]["name"],
            "avatar": payload.get("sender", {}).get("avatar_url", ""),  # ⭐ add avatar
            "type": "push",
            "to_branch": payload["ref"].split("/")[-1],
            "from_branch": None,
            "timestamp": payload["head_commit"]["timestamp"]
        }

    elif event_type == "pull_request":
        pr = payload["pull_request"]
        event = {
            "author": pr["user"]["login"],
            "avatar": pr["user"].get("avatar_url", ""),  # ⭐ add avatar
            "type": "pull_request",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": pr["created_at"]
        }

    else:
        return jsonify({"msg": "Unsupported event"}), 400

    collection.insert_one(event)
    return jsonify({"msg": "Event stored"}), 200


@app.route('/events')
def get_events():
    try:
        events = list(collection.find().sort("_id", -1).limit(10))
        return jsonify([format_event(e) for e in events])
    except Exception as e:
        print("Error fetching events:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
