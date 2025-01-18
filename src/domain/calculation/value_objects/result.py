# endregion-------------------------------------------------------------------------
# region CALCULATION RESULT VALUE OBJECT
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from decimal import Decimal

from domain.common.value_object import ValueObjectBase


@dataclass(frozen=True)
class CalculationResult(ValueObjectBase[Decimal]):
    def validate(self):
        pass

    def as_raw(self) -> Decimal:
        return self._value


# endregion-------------------------------------------------------------------------
