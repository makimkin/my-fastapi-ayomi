# endregion-------------------------------------------------------------------------
# region CALCULATION COMPUTE COMMAND
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from application.common.command import CommandBase, CommandHandlerBase

from domain.calculation.value_objects import CalculationExpression, CalculationResult
from domain.calculation.entity import CalculationEntity

from infrastructure.calculators.base import CalculatorBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CalculationComputeCommand(CommandBase):
    expression: str


@dataclass(frozen=True)
class CalculationComputeCommandHandler(
    CommandHandlerBase[
        CalculationComputeCommand,
        CalculationEntity,
    ]
):
    calculator: CalculatorBase

    async def _handle(
        self,
        command: CalculationComputeCommand,
    ) -> CalculationEntity:
        expression = CalculationExpression(command.expression)
        result = await self.calculator.compute(expression)

        return CalculationEntity(
            expression=expression,
            result=CalculationResult(result),
        )


# endregion-------------------------------------------------------------------------
