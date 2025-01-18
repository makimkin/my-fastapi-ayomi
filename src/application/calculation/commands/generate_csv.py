# endregion-------------------------------------------------------------------------
# region CALCULATION GENERATE CSV COMMAND
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from application.common.command import CommandBase, CommandHandlerBase

from infrastructure.csv_builder.calculations.base import CalculationsCSVBuilderBase
from infrastructure.repositories.calculation.base import CalculationRepositoryBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CalculationGenerateCSVCommand(CommandBase):
    pass


@dataclass(frozen=True)
class CalculationGenerateCSVCommandHandler(
    CommandHandlerBase[
        CalculationGenerateCSVCommand,
        str,
    ]
):
    calculations_repository: CalculationRepositoryBase
    calculations_csv_builder: CalculationsCSVBuilderBase

    async def _handle(
        self,
        _: CalculationGenerateCSVCommand,
    ) -> str:
        calculations = await self.calculations_repository.get_many()

        return await self.calculations_csv_builder.build(calculations)


# endregion-------------------------------------------------------------------------
