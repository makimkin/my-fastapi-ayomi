# endregion-------------------------------------------------------------------------
# region BASE VALUE OBJECTS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObjectBase[V](ABC):
    _value: V

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self): ...

    @abstractmethod
    def as_raw(self) -> V: ...


# endregion-------------------------------------------------------------------------
