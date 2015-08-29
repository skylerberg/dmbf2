from random import randint

from dmbf2 import models


def make_random_person(world):
    trait_ = trait()
    occupation_ = occupation()

    person = models.Person(
        first_name="Skyler",
        last_name=last_name(),
        age=22,
        world_id=world.id,
        trait_id=trait_.id,
        occupation_id=occupation_.id)

    return person


def last_name():
    return "Berg"


def male_first_name():
    pass


def female_first_name():
    pass


def trait():
    return models.Trait(name="nice")


def occupation():
    return models.Occupation(name="software developer")


def gender():
    if randint(0, 1):
        return "male"
    else:
        "female"
