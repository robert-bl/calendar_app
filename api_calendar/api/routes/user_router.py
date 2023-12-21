from flask import Blueprint, request, jsonify

from extensions import db
from models import User, user_schema, users_schema

user_routes = Blueprint('user', __name__, url_prefix='/users')


@user_routes.route('/create', methods=['POST'])
def create_user():
    name = request.json['name']
    password = request.json['password']

    new_user = User(name=name, password=password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@user_routes.route('/get/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)