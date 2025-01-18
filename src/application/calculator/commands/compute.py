# endregion-------------------------------------------------------------------------
# region CALCULATOR COMPUTE COMMAND
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from decimal import Decimal

from application.common.command import CommandBase, CommandHandlerBase

from infrastructure.calculators.base import CalculatorBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CalculatorComputeCommandDTO:
    expression: str
    result: Decimal


@dataclass(frozen=True)
class CalculatorComputeCommand(CommandBase):
    expression: str


@dataclass(frozen=True)
class CalculatorComputeCommandHandler(
    CommandHandlerBase[
        CalculatorComputeCommand,
        CalculatorComputeCommandDTO,
    ]
):
    calculator: CalculatorBase

    async def _handle(
        self,
        command: CalculatorComputeCommand,
    ) -> CalculatorComputeCommandDTO:
        return CalculatorComputeCommandDTO(
            expression=command.expression,
            result=await self.calculator.compute(command.expression),
        )


# endregion-------------------------------------------------------------------------
