# endregion-------------------------------------------------------------------------
# region CALCULATION DOMAIN EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.common.exceptions import DomainValueObjectException


@dataclass(frozen=False)
class CalculationExpressionInvalidCharacterException(DomainValueObjectException):
    char: str

    @property
    def message(self) -> str:
        return f"Invalid character '{self.char}' found in expression"


# endregion-------------------------------------------------------------------------
