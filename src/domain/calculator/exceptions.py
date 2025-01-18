# endregion-------------------------------------------------------------------------
# region CALCULATOR DOMAIN EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.common.exceptions import DomainValueObjectException


@dataclass(frozen=False)
class CalculatorExpressionInvalidCharacterException(DomainValueObjectException):
    char: str

    @property
    def message(self) -> str:
        return f"Invalid character '{self.char}' found in expression"


# endregion-------------------------------------------------------------------------
