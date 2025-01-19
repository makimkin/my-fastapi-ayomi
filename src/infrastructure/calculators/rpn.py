# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from decimal import Decimal

from domain.calculation.value_objects import (
    CalculationExpression,
    CalculationOperands,
)

from infrastructure.calculators.base import CalculatorBase
from infrastructure.calculators.exceptions import (
    CalculatorOperandHandlerUnfoundException,
    CalculatorExpressionInvalidException,
    CalculatorDivisionByZeroException,
)

logger = logging.getLogger("app")


@dataclass
class CalculatorRPN(CalculatorBase):
    OPERANDS = {
        CalculationOperands.SUBTRACT: lambda e1, e2: e1 - e2,
        CalculationOperands.MULTIPLY: lambda e1, e2: e1 * e2,
        CalculationOperands.DIVIDE: lambda e1, e2: e1 / e2,
        CalculationOperands.ADD: lambda e1, e2: e1 + e2,
    }

    async def compute(self, expression: CalculationExpression) -> Decimal:
        stack = []

        for element in expression.to_list():
            if isinstance(element, Decimal):
                stack.append(element)
                continue

            if len(stack) < 2:
                raise CalculatorExpressionInvalidException()

            x2, x1 = stack.pop(), stack.pop()

            if x2 == 0 and element == CalculationOperands.DIVIDE:
                raise CalculatorDivisionByZeroException(expression.as_raw())

            try:
                operand = self.OPERANDS[element]
            except KeyError as e:
                raise CalculatorOperandHandlerUnfoundException(element.value) from e

            stack.append(operand(x1, x2))

        return stack.pop()

    async def check_health(self) -> bool:
        expression = CalculationExpression("1 1 +")

        return await self.compute(expression) == 2


# endregion-------------------------------------------------------------------------
