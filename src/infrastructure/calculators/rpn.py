# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from decimal import Decimal

from domain.calculator.value_objects import CalculatorExpression, CalculatorOperands

from infrastructure.calculators.base import CalculatorBase
from infrastructure.calculators.exceptions import (
    CalculatorExpressionInvalidException,
)

logger = logging.getLogger("app")


@dataclass
class CalculatorRPN(CalculatorBase):
    OPERANDS = {
        CalculatorOperands.SUBTRACT: lambda e1, e2: e1 - e2,
        CalculatorOperands.MULTIPLY: lambda e1, e2: e1 * e2,
        CalculatorOperands.DIVIDE: lambda e1, e2: e1 / e2,
        CalculatorOperands.ADD: lambda e1, e2: e1 + e2,
    }

    async def compute(self, expression: CalculatorExpression) -> Decimal:
        stack = []

        for element in expression.to_list():
            if element in self.OPERANDS:
                if len(stack) < 2:
                    raise CalculatorExpressionInvalidException()

                x2, x1 = stack.pop(), stack.pop()

                stack.append(self.OPERANDS[element](x1, x2))
                continue

            stack.append(element)

        return stack.pop()

    async def check_health(self) -> bool:
        expression = CalculatorExpression("1 1 +")

        return await self.compute(expression) == 2


# endregion-------------------------------------------------------------------------
