from flask import Blueprint, request, jsonify
from . import db
from .models import User
from .schemas import user_schema, users_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = User(
        name=data['name'],
        age=data['age'],
        address=data['address']
    )
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@api.route('/users', methods=['GET'])
def get_users():
    search = request.args.get('search', type=str)
    sort_by = request.args.get('sort_by', type=str)
    order = request.args.get('order', 'asc')

    query = User.query
    if search:
        query = query.filter(User.name.ilike(f"%{search}%"))
    if sort_by == 'name':
        query = query.order_by(User.name.desc() if order=='desc' else User.name.asc())
    elif sort_by == 'points':
        query = query.order_by(User.points.desc() if order=='desc' else User.points.asc())

    users = query.all()
    return users_schema.jsonify(users)

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.name = data.get('name', user.name)
    user.age = data.get('age', user.age)
    user.points = data.get('points', user.points)
    user.address = data.get('address', user.address)
    db.session.commit()
    return user_schema.jsonify(user)

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
