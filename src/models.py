from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="user")

class Character(db.Model):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[str] = mapped_column(String(50))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    species: Mapped[str] = mapped_column(String(50))

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="character")
    planet: Mapped["Planet"] = relationship(back_populates="characters")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "planet_id": self.planet_id,
            "species": self.species,
        }

class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    population: Mapped[str] = mapped_column(String(50))
    climate: Mapped[str] = mapped_column(String(50))
    classification: Mapped[str] = mapped_column(String(50))

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="planet")
    characters: Mapped[list["Character"]] = relationship(back_populates="planet")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "classification": self.classification,
        }

class Favorite(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))

    user: Mapped["User"] = relationship(back_populates="favorites")
    character: Mapped["Character"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }