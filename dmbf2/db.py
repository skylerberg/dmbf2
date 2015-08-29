from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dmbf2 import models


engine = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    models.Base.metadata.create_all(engine)


def create_world(name):
    world = models.World(name=name)
    session.add(world)
    session.commit()


def add_person(person):
    session.add(person)
    session.commit()
