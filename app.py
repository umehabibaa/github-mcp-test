from flask import Flask, request, jsonify
from database import get_user
from auth import check_password

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    user = get_user(username)

    if user and check_password(password, user["password"]):
        return jsonify({"message": "Login successful"})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/users/<username>")
def get_profile(username):
    user = get_user(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "username": user["username"],
        "email": user["email"]
    })


if __name__ == "__main__":
    app.run(debug=True)
