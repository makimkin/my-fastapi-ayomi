# endregion-------------------------------------------------------------------------
# region BASE VALUE OBJECTS
# ----------------------------------------------------------------------------------
import datetime

from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID, uuid4

from domain.common.exceptions import EntityIdIncorrectValueException

from lib.dt import convert_datetime_to_ms, convert_ms_to_datetime


# endregion-------------------------------------------------------------------------
# region BASE
# ----------------------------------------------------------------------------------
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
# region ID
# ----------------------------------------------------------------------------------
@dataclass(frozen=True)
class EntityId(ValueObjectBase[str]):
    def validate(self):
        try:
            UUID(self._value)
        except (ValueError, TypeError) as e:
            raise EntityIdIncorrectValueException(value=self._value) from e

    @classmethod
    def create(cls) -> "EntityId":
        return EntityId(_value=str(uuid4()))

    def as_raw(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self.as_raw()


# endregion-------------------------------------------------------------------------
# region CREATED AT
# ----------------------------------------------------------------------------------
@dataclass(frozen=True)
class EntityCreatedAt(ValueObjectBase[int]):
    def validate(self):
        pass

    @classmethod
    def create(cls) -> "EntityCreatedAt":
        return EntityCreatedAt(
            _value=convert_datetime_to_ms(datetime.datetime.now())
        )

    def as_raw(self) -> int:
        return self._value

    def as_datetime(self) -> datetime.datetime:
        return convert_ms_to_datetime(self._value)


# endregion-------------------------------------------------------------------------
