# endregion-------------------------------------------------------------------------
# region CALCULATORS EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.exceptions import DomainExceptionBase


@dataclass(frozen=False)
class CalculatorExpressionInvalidException(DomainExceptionBase):
    @property
    def message(self) -> str:
        return "Calculator expression is invalid"


# endregion-------------------------------------------------------------------------
