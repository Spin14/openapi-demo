# this file will abstract the how
# our data is stored from the rest
# of the code.
import json
import logging
from typing import Any, Dict, List, Optional

from .logging import logger as persons_logger
from .models import PersonModel


class DB:
    def __init__(self, logger: Optional[logging.Logger] = None) -> None:
        # we will use a dict as our db
        self._storage: Dict[int, PersonModel] = {}
        self.logger: logging.Logger = logger if logger is not None else logging.getLogger("dummy")

    def _load_person(self, raw: Dict[str, Any]) -> Optional[PersonModel]:
        person: Optional[PersonModel] = None
        try:
            person = PersonModel(person_id=raw["id"], name=raw["name"], age=raw["age"], beautiful=raw["beautiful"])
        except KeyError as e:
            # a missing key in our raw data
            self.logger.warning(f"Failed to load person: missing key: {str(e)}")

        return person

    def _read_file(self, filepath: str) -> List[Dict[str, Any]]:
        try:
            with open(filepath) as f:
                return json.load(f)
        except FileNotFoundError as e:
            self.logger.error(f"Failed to read fixtures: {str(e)}")
            return []

    def setup(self, filepath: str) -> None:
        """Populates our db.
        """
        raw_persons = self._read_file(filepath)

        for raw_person in raw_persons:
            person = self._load_person(raw_person)
            if person is not None:
                self._storage[person.person_id] = person

        self.logger.info(f"added {len(self._storage)} persons to the database")

    def teardown(self) -> None:
        self._storage = {}
        self.logger.info(f"database cleared")

    def list_persons(self) -> List[PersonModel]:
        # _ is used whenever you are not going to use a variable
        return [person for _, person in self._storage.items()]

    def create_person(self, *, name: str, age: int, beautiful: bool) -> PersonModel:
        person_id = 1
        while True:  # this is really not efficient but lets look away
            if person_id not in self._storage:
                break
            person_id += 1

        person = PersonModel(person_id=person_id, name=name, age=age, beautiful=beautiful)
        self._storage[person.person_id] = person
        return person

    def get_person(self, person_id: int) -> Optional[PersonModel]:
        return self._storage.get(person_id, None)

    def update_person(self, person_id: int, *, name: str, age: int) -> Optional[PersonModel]:
        """I decided that beautiful can't be updated in this case
        """
        person = self._storage.get(person_id, None)
        if person is not None:
            person = person.copy(name=name, age=age)
            self._storage[person_id] = person

        return person

    def delete_person(self, person_id: int) -> bool:
        person = self._storage.pop(person_id, None)
        return True if person is not None else False


def get_db() -> DB:
    return DB(persons_logger)


db = get_db()
