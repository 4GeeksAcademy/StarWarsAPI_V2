from flask import jsonify, request
from models import db, Character
from sqlalchemy import select

def register_character_routes(app):

    @app.route("/characters", methods=["GET"])
    def characters_collection():
        if request.method == "GET":
            characters = db.session.execute(select(Character)).scalars().all()
            result = [character.serialize() for character in characters]
            return jsonify(result), 200

    @app.route("/character/<int:character_id>", methods=["GET"])
    def character_item(character_id):
        character = db.session.get(Character, character_id)
        if not character:
            return {"error": "Character not found"}, 404
        if request.method == "GET":
            result = character.serialize()
            return jsonify(result), 200