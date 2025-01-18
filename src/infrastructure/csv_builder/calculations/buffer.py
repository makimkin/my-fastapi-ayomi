# endregion-------------------------------------------------------------------------
# region CALCULATIONS BUFFER CSV BUILDER CLASS
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from domain.calculation.entity import CalculationEntity
from infrastructure.csv_builder.common.buffer import CSVBuilderBuffer

from .base import CalculationsCSVBuilderBase

logger = logging.getLogger("app")


@dataclass
class CalculationsCSVBuilderBuffer(
    CalculationsCSVBuilderBase,
    CSVBuilderBuffer[CalculationEntity],
):
    async def check_health(self) -> bool:
        return True


# endregion-------------------------------------------------------------------------
