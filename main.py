from flask import Flask, jsonify, request
from business.user_service import UserService
from presentation.user_controller import UserController
from business.model.user import User

app = Flask(__name__)
user_service = UserService()
user_controller = UserController(user_service)


@app.route("/")
def hello_world():
    return "I am OK."


@app.route("/user", methods = ['POST'])
def user():
    incoming_data = request.get_json(force=True)
    user_data = user_controller.create_user(incoming_data)
    return jsonify(user_data)

@app.route("/user/user_id")
def get_user(user_id):
    user_data = user_controller.get_user(user_id)
    return jsonify(user_data)

    


if __name__ == "__main__":
    app.run(debug=True)
