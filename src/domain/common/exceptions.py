# endregion-------------------------------------------------------------------------
# region DOMAIN COMMON EXCEPTIONS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.exceptions import DomainExceptionBase


# endregion-------------------------------------------------------------------------
# region VALUE OBJECT EXCEPTIONS
# ----------------------------------------------------------------------------------
@dataclass(frozen=False)
class DomainValueObjectException(DomainExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Domain value object error occured"


@dataclass(frozen=False)
class EntityIdIncorrectValueException(DomainValueObjectException):
    value: str

    @property
    def message(self) -> str:
        return f"EntityId value is incorrect: {self.value}"


# endregion-------------------------------------------------------------------------
