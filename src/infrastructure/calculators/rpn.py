# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR
# ----------------------------------------------------------------------------------
import logging

from decimal import Decimal, InvalidOperation
from dataclasses import dataclass

from infrastructure.calculators.base import CalculatorBase

logger = logging.getLogger("app")


@dataclass
class CalculatorRPN(CalculatorBase):
    OPERANDS = {
        "-": lambda e1, e2: e1 - e2,
        "*": lambda e1, e2: e1 * e2,
        "/": lambda e1, e2: e1 / e2,
        "+": lambda e1, e2: e1 + e2,
    }

    async def compute(self, expression: str) -> Decimal:
        items = expression.strip().split(" ")

        stack = []

        for i in items:
            if (number := self._check_if_number(i)) is not None:
                stack.append(number)
                continue

            if i in self.OPERANDS:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")

                x2 = stack.pop()
                x1 = stack.pop()

                stack.append(self.OPERANDS[i](x1, x2))
                continue

            raise ValueError("Invalid expression")

        return stack.pop()

    def _check_if_number(self, value: str) -> Decimal | None:
        try:
            return Decimal(value)
        except InvalidOperation:
            return None

    async def check_health(self) -> bool:
        return await self.compute("1 1 +") == 2


# endregion-------------------------------------------------------------------------
