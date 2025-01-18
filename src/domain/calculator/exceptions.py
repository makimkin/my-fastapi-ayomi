# endregion-------------------------------------------------------------------------
# region CALCULATOR DOMAIN EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.exceptions import DomainExceptionBase


@dataclass(frozen=False)
class CalculatorExpressionInvalidCharacterException(DomainExceptionBase):
    char: str

    @property
    def message(self) -> str:
        return f"Invalid character '{self.char}' found in expression"


# endregion-------------------------------------------------------------------------
