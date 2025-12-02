from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_USERS = "http://service-users:5001"
SERVICE_PRODUCTS = "http://service-products:5002"
SERVICE_ORDERS = "http://service-orders:5003"

@app.route("/")
def root():
    return jsonify({"message": "API Gateway ativo!"})

@app.route("/users")
def users():
    response = requests.get(f"{SERVICE_USERS}/users")
    return jsonify(response.json())

@app.route("/products")
def products():
    response = requests.get(f"{SERVICE_PRODUCTS}/products")
    return jsonify(response.json())

@app.route("/orders")
def orders():
    response = requests.get(f"{SERVICE_ORDERS}/orders")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
