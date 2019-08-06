from persons.models import Error, PersonModel


def test_person_args_kwargs() -> None:
    person_args = PersonModel(10, "Test 10", 10, False)
    person_kwargs = PersonModel(person_id=10, name="Test 10", age=10, beautiful=False)
    assert person_args == person_kwargs


def test_person_dict() -> None:
    person = PersonModel(person_id=10, name="Test 10", age=10, beautiful=False)

    expected_dict = {"person_id": 10, "name": "Test 10", "age": 10, "beautiful": False}

    assert person.as_dict() == expected_dict


def test_error_args_kwargs() -> None:
    err_args = Error(404, "not found")
    err_kwargs = Error(code=404, message="not found")
    assert err_args == err_kwargs


def test_error_dict() -> None:
    err = Error(code=404, message="not found")

    expected_dict = {"code": 404, "message": "not found"}

    assert err.as_dict() == expected_dict
