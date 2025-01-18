# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from infrastructure.calculators.base import CalculatorBase

logger = logging.getLogger("app")


@dataclass
class CalculatorRPN(CalculatorBase):
    async def compute(self, expression: str) -> float:
        return len(expression)

    async def check_health(self) -> bool:
        return True


# endregion-------------------------------------------------------------------------
