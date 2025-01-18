# endregion-------------------------------------------------------------------------
# region CALCULATION MEMORY REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.calculator.entity import CalculatorEntity

from infrastructure.repositories.common.memory import RepositoryMemory

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositoryMemory(
    CalculationRepositoryBase,
    RepositoryMemory[CalculatorEntity],
):
    async def save_one(self, calculator: CalculatorEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculator.
        -------------------------------------------------------------------------"""
        self._saved.append(calculator)

    async def get_many(self) -> list[CalculatorEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        return self.saved


# endregion-------------------------------------------------------------------------
