from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 65000},
    {"id": 2, "name": "Phone", "price": 30000},
    {"id": 3, "name": "Headphones", "price": 3000}
]


@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next(
        (product for product in products if product["id"] == product_id),
        None
    )

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(new_product)

    return jsonify(new_product), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)