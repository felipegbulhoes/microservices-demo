from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    # Consumindo service-users
    users = requests.get("http://service-users:5001/users").json()

    # Consumindo service-products
    products = requests.get("http://service-products:5002/products").json()

    # Montando um pedido simples
    order = {
        "order_id": 1,
        "user": users[0],
        "product": products[0],
        "status": "processed"
    }

    return jsonify(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
