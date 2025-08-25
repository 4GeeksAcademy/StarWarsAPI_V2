from flask import jsonify, request
from models import db, Planet
from sqlalchemy import select

def register_planet_routes(app):

    @app.route("/planets", methods=["GET"])
    def planets_collection():
        if request.method == "GET":
            planets = db.session.execute(select(Planet)).scalars().all()
            result = [planet.serialize() for planet in planets]
            return jsonify(result), 200

    @app.route("/planet/<int:planet_id>", methods=["GET"])
    def planet_item(planet_id):
        planet = db.session.get(Planet, planet_id)
        if not planet:
            return {"error": "Planet not found"}, 404
        if request.method == "GET":
            result = planet.serialize()
            return jsonify(result), 200