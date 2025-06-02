#Your CRUD Blueprint:

from flask import Blueprint,request,jsonify
from .utils import read_users,write_users

users_bp = Blueprint('users',__name__)

#Get all users:
@users_bp.route('/users',methods = ['GET'])
def get_users():
  return jsonify(read_users())

#Get a user(with id):
@users_bp.route('/users/<int:user_id>',methods = ['GET'])
def get_user(user_id):
  users = read_users()
  user = next((u for u in users if u["id"]==user_id),None)
  return jsonify(user) if user else (jsonify({"error":"user not found!"}),404)

#Create a user:
@users_bp.route('/users',methods = ['POST'] )
def create_user():
  users = read_users()
  data = request.json
  if not data.get("name") or not data.get("email"):
    return jsonify({"error": "Name and email are required"}), 400
  
  new_user = {
    "id": users[-1]["id"]+1 if users else 1,
    "name": data["name"],
    "email": data["emails"]
  }
  users.append(new_user)
  write_users(users)
  return jsonify(new_user)

#Update a user:(PUT)
@users_bp.route('/users<int:user_id>',methods = ['PUT'])
def update_user(user_id):
  users = read_users()
  user = next((u for u in users if u["id"]==user_id),None)
  if not user:
     return jsonify({"error": "User not found"}), 404
  
  data = request.json
  user["name"] = data.get("name",data["name"])
  user["email"] = data.get("email",data["email"])
  write_users(users)
  return jsonify(user)

#Delete a user:
@users_bp.route('/users/<int:user_id>',methods = ['DELETE'])
def delete_user(user_id):
  users = read_users()
  updated_users = [u for u in users if u["id"]!=user_id]

  if len(updated_users) == len(users):
    return jsonify({"error":"User not found"}),404
  
  write_users(updated_users)
  return jsonify({"message": f"User {user_id} is deleted."})
