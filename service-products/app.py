from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados simples em memória
products = [
    {"id": 1, "name": "Notebook", "price": 3500},
    {"id": 2, "name": "Mouse", "price": 80},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
