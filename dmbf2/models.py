from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return "<World(name='%s')>" % (self.name)


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    world_id = Column(Integer, ForeignKey('worlds.id'))
    occupation_id = Column(Integer, ForeignKey('occupations.id'))
    trait_id = Column(Integer, ForeignKey('traits.id'))

    world = relationship("World", backref=backref('people', order_by=id))
    occupation = relationship("Occupation",
                              backref=backref('occupations', order_by=id))
    trait = relationship("Trait", backref=backref('traits', order_by=id))


class Trait(Base):
    __tablename__ = 'traits'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Occupation(Base):
    __tablename__ = 'occupations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
