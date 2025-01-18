# endregion-------------------------------------------------------------------------
# region CALCULATOR EXPRESSION VALUE OBJECT
# ----------------------------------------------------------------------------------
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from enum import Enum

from domain.common.value_object import ValueObjectBase

from ..exceptions import CalculatorExpressionInvalidCharacterException


class CalculatorOperands(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


@dataclass(frozen=True)
class CalculatorExpression(ValueObjectBase[str]):
    def validate(self):
        object.__setattr__(self, "_value", self._value.strip())

        for e in self._value.split(" "):
            if self._try_to_convert(e) is not None:
                continue

            if e in ["+", "-", "*", "/"]:
                continue

            raise CalculatorExpressionInvalidCharacterException(e)

    def _try_to_convert(self, e: str) -> Decimal | None:
        try:
            return Decimal(e)
        except InvalidOperation:
            return None

    def to_list(self) -> list[Decimal | CalculatorOperands]:
        elements = []

        for e in self._value.split(" "):
            if (n := self._try_to_convert(e)) is not None:
                elements.append(n)
                continue

            elements.append(CalculatorOperands(e))

        return elements

    def as_raw(self) -> str:
        return self._value


# endregion-------------------------------------------------------------------------
