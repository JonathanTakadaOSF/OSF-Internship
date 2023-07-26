from flask import Blueprint, jsonify, request
from models import User, Purchases
from peewee import JOIN

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = list(User.select().dicts())
    return users
    #return jsonify([{"id": user.id, "name": user.name} for user in users])

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name})
    else:
        return jsonify({"error": "User not found"}), 404

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User.create(id=data.get('id'), name=data.get('name'))
    return jsonify({"id": new_user.id, "name": new_user.name}), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        data = request.get_json()
        user.name = data.get('name', user.name)
        user.save()
        return jsonify({"id": user.id, "name": user.name})
    else:
        return jsonify({"error": "User not found"}), 404

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        user.delete_instance()
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

@users_bp.route('/users/purchases/', methods=['GET'])
def get_user_purchases():
    users = list(User.select(User.name.alias('user_name'), Purchases.name.alias('purchase_name'))
             .join(Purchases, join_type=JOIN.LEFT_OUTER, on=(User.id == Purchases.user_id))
             .dicts())
    
    return users

@users_bp.route('/users/purchases/<int:user_id>', methods=['GET'])
def get_user_purchases_per_id(user_id):
    users = list(User.select(User.name.alias('user_name'), Purchases.name.alias('purchase_name'))
             .join(Purchases, join_type=JOIN.LEFT_OUTER, on=(User.id == Purchases.user_id))
             .where(Purchases.user_id==user_id)
             .dicts())
    
    return users
