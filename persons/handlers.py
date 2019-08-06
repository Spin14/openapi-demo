from typing import Any, List, Optional, Union

from .db import db
from .models import ErrorDict, PersonDict, PersonModel, error400, error404

PersonOrErrorDict = Union[PersonDict, ErrorDict]


def _person_or_404(person: Optional[PersonModel]) -> PersonOrErrorDict:
    if person is not None:
        return person.as_dict()
    return error404.as_dict()


def list_persons() -> List[PersonDict]:
    return [person.as_dict() for person in db.list_persons()]


# def create_person(*, name: str, age: str, beautiful: bool) -> PersonDict:
def create_person(body: Any) -> PersonDict:
    try:
        person = db.create_person(name=body["name"], age=body["age"], beautiful=body["beautiful"])
    except KeyError:
        # empty body is not validated by connexion, dunno why
        return error400.as_dict()
    return person.as_dict()


def retrieve_person(person_id: int) -> PersonOrErrorDict:
    person = db.get_person(person_id)
    return _person_or_404(person)


def update_person(person_id: int, body: Any) -> PersonOrErrorDict:
    try:
        person = db.update_person(person_id, name=body["name"], age=body["age"])
    except KeyError:
        # empty body is not validated by connexion, dunno why
        return error400.as_dict()
    return _person_or_404(person)


def delete_person(person_id: int) -> Union[None, ErrorDict]:
    success = db.delete_person(person_id)
    # this is not working properly
    # from connexion import NoContent ? I will investigate latter
    return None if success else error400.as_dict()
