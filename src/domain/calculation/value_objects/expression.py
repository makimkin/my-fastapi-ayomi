# endregion-------------------------------------------------------------------------
# region CALCULATION EXPRESSION VALUE OBJECT
# ----------------------------------------------------------------------------------
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from enum import Enum

from domain.common.value_object import ValueObjectBase

from ..exceptions import CalculationExpressionInvalidCharacterException


class CalculationOperands(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


@dataclass(frozen=True)
class CalculationExpression(ValueObjectBase[str]):
    def validate(self):
        object.__setattr__(self, "_value", self._value.strip())

        for e in self._value.split(" "):
            if self._try_to_convert(e) is not None:
                continue

            if e in ["+", "-", "*", "/"]:
                continue

            raise CalculationExpressionInvalidCharacterException(e)

    def _try_to_convert(self, e: str) -> Decimal | None:
        try:
            return Decimal(e)
        except InvalidOperation:
            return None

    def to_list(self) -> list[Decimal | CalculationOperands]:
        elements = []

        for e in self._value.split(" "):
            if (n := self._try_to_convert(e)) is not None:
                elements.append(n)
                continue

            elements.append(CalculationOperands(e))

        return elements

    def as_raw(self) -> str:
        return self._value


# endregion-------------------------------------------------------------------------
