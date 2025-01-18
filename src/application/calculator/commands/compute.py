# endregion-------------------------------------------------------------------------
# region CALCULATOR COMPUTE COMMAND
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from application.common.command import CommandBase, CommandHandlerBase

from domain.calculator.value_objects import CalculatorExpression, CalculatorResult
from domain.calculator.entity import CalculatorEntity

from infrastructure.calculators.base import CalculatorBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CalculatorComputeCommand(CommandBase):
    expression: str


@dataclass(frozen=True)
class CalculatorComputeCommandHandler(
    CommandHandlerBase[
        CalculatorComputeCommand,
        CalculatorEntity,
    ]
):
    calculator: CalculatorBase

    async def _handle(
        self,
        command: CalculatorComputeCommand,
    ) -> CalculatorEntity:
        result = await self.calculator.compute(command.expression)

        return CalculatorEntity(
            expression=CalculatorExpression(command.expression),
            result=CalculatorResult(result),
        )


# endregion-------------------------------------------------------------------------
