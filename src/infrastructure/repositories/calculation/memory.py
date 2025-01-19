# endregion-------------------------------------------------------------------------
# region CALCULATION MEMORY REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.calculation.entity import CalculationEntity

from infrastructure.repositories.common.memory import RepositoryMemory

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositoryMemory(
    CalculationRepositoryBase,
    RepositoryMemory[CalculationEntity],
):
    async def save_one(self, calculation: CalculationEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculation.
        -------------------------------------------------------------------------"""
        self._saved.append(calculation)

    async def get_many(
        self,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculations.
        -------------------------------------------------------------------------"""
        return (
            self.saved[offset : offset + limit]
            if limit is not None
            else self.saved[offset:]
        )


# endregion-------------------------------------------------------------------------
