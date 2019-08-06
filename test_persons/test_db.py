from persons.db import DB
from persons.models import PersonModel


def test_list_persons(db: DB) -> None:
    persons = db.list_persons()

    for person in persons:
        assert isinstance(person, PersonModel)

    assert len(persons) == 3


def test_create_person(db: DB) -> None:
    person = db.create_person(name="Barnabe", age=0, beautiful=True)
    assert isinstance(person, PersonModel)
    assert person.person_id not in [1, 2, 3]
    assert person.name == "Barnabe"
    assert person.age == 0
    assert person.beautiful is True


def test_get_person(db: DB) -> None:
    person_1 = db.get_person(1)
    assert isinstance(person_1, PersonModel)
    assert person_1.person_id == 1
    assert person_1.name == "Test 1"

    person_2 = db.get_person(2)
    assert isinstance(person_2, PersonModel)
    assert person_2.person_id == 2
    assert person_2.name == "Test 2"

    assert db.get_person(99) is None


def test_update_person(db: DB) -> None:
    person = db.update_person(1, name="Updated!", age=100)
    assert isinstance(person, PersonModel)
    assert person.person_id == 1
    assert person.name == "Updated!"

    assert db.update_person(99, name="-", age=100) is None


def test_delete_person(db: DB) -> None:
    deleted = db.delete_person(1)
    assert deleted is True

    assert db.delete_person(1) is False

    assert db.delete_person(99) is False
