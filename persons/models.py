from dataclasses import asdict, dataclass, replace
from typing import Any, Dict, Union

PersonDict = Dict[str, Union[int, str, bool]]

ErrorDict = Dict[str, Union[int, str]]


@dataclass
class PersonModel:
    person_id: int
    name: str
    age: int
    beautiful: bool

    def as_dict(self) -> PersonDict:
        return asdict(self)

    def copy(self, **kwargs: Any) -> "PersonModel":
        return replace(self, **kwargs)


@dataclass
class Error:
    code: int
    message: str

    def as_dict(self) -> ErrorDict:
        return asdict(self)


error400 = Error(code=400, message="validation error")
error404 = Error(code=404, message="person not found")
error505 = Error(code=500, message="internal server error")
