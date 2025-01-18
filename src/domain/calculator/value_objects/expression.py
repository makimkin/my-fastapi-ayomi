# endregion-------------------------------------------------------------------------
# region CALCULATOR EXPRESSION VALUE OBJECT
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.common.value_object import ValueObjectBase


@dataclass(frozen=True)
class CalculatorExpression(ValueObjectBase[str]):
    def validate(self):
        object.__setattr__(self, "_value", self._value.strip())

    def as_raw(self) -> str:
        return self._value


# endregion-------------------------------------------------------------------------
