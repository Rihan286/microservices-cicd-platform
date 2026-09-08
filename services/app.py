from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = [
    {
        "id": 1,
        "user_id": 1,
        "message": "Your order has been confirmed",
        "status": "sent"
    },
    {
        "id": 2,
        "user_id": 2,
        "message": "Your order is being processed",
        "status": "pending"
    }
]


@app.route("/")
def home():
    return jsonify({
        "service": "Notification Service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/notifications", methods=["GET"])
def get_notifications():
    return jsonify(notifications)


@app.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    notification = next(
        (
            notification
            for notification in notifications
            if notification["id"] == notification_id
        ),
        None
    )

    if notification is None:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify(notification)


@app.route("/notifications", methods=["POST"])
def create_notification():
    data = request.get_json()

    new_notification = {
        "id": len(notifications) + 1,
        "user_id": data["user_id"],
        "message": data["message"],
        "status": "pending"
    }

    notifications.append(new_notification)

    return jsonify(new_notification), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)