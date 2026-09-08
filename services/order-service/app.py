from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {
        "id": 1,
        "user_id": 1,
        "product_id": 2,
        "quantity": 1,
        "status": "confirmed"
    },
    {
        "id": 2,
        "user_id": 2,
        "product_id": 1,
        "quantity": 2,
        "status": "pending"
    }
]


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = next(
        (order for order in orders if order["id"] == order_id),
        None
    )

    if order is None:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    new_order = {
        "id": len(orders) + 1,
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "quantity": data["quantity"],
        "status": "pending"
    }

    orders.append(new_order)

    return jsonify(new_order), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)