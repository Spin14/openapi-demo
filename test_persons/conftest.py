from typing import Generator

import pytest

from persons.db import DB, get_db


@pytest.fixture()
def db() -> Generator[DB, None, None]:
    db = get_db()
    db.setup("fixtures/testing.json")
    yield db
    db.teardown()
