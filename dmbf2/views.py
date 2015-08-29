import json

from flask import request, redirect, url_for
from flask import render_template

from dmbf2 import app
from dmbf2 import db
from dmbf2 import generator
from models import World, Person


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html.jinja",
                           worlds=db.session.query(World).all())


@app.route("/world", methods=["POST", "PUT"])
def create_world():
    data = request.form
    if "name" not in data:
        raise Exception("Should have name")
    db.create_world(data["name"])
    return redirect(url_for("home"))


@app.route("/world", methods=["DELETE"])
def delete_world():
    data = json.loads(request.data)
    if "name" not in request.data:
        raise Exception("Should have name")
    db.delete_world(data)
    return ""


@app.route("/worlds/<world>/", methods=["GET"])
def get_world(world=None):
    world = db.session.query(World).filter(World.name == world).one()
    people = db.session.query(Person).filter(Person.world_id == world.id).all()
    return render_template("world.html.jinja",
                           world=world,
                           people=people)


@app.route("/worlds/<world>/people/<person>", methods=["GET"])
def get_person(world=None, person=None):
    person = db.session.query(Person).filter(World.id == world).filter(Person.id == person).one()
    world = db.session.query(World).filter(World.id == world).one()
    return render_template("person.html.jinja", world=world, person=person)


@app.route("/worlds/<world>/create_person", methods=["POST", "PUT"])
def create_person(world=None):
    world = db.session.query(World).filter(World.name == world).one()
    db.session.add(generator.make_random_person(world))
    db.session.commit()
    return ""
