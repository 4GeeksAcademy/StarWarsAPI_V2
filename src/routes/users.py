from flask import jsonify, request
from models import db,  User, Favorite, Planet, Character
from sqlalchemy import select

def register_user_routes(app):

    @app.route("/users", methods=["GET"])
    def app_users():
        if request.method == "GET":
            users = db.session.execute(select(User)).scalars().all()
            result = [user.serialize() for user in users]
            return jsonify(result), 200
        
    @app.route("/users/favorites", methods=["GET"])
    def user_favorites():
        if request.method == "GET":
            user = db.session.get(User, user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404
            favorites = db.session.execute(select(Favorite)).scalars().all()
            result = [favorite.serialize() for favorite in favorites]
            return jsonify(result), 200

