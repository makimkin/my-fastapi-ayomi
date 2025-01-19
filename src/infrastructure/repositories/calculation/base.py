# endregion-------------------------------------------------------------------------
# region CALCULATION BASE REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.calculation.entity import CalculationEntity

from ..common.base import RepositoryBase


@dataclass
class CalculationRepositoryBase(RepositoryBase, ABC):
    @abstractmethod
    async def save_one(self, calculation: CalculationEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculation.
        -------------------------------------------------------------------------"""
        ...

    @abstractmethod
    async def get_many(
        self,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculations.
        -------------------------------------------------------------------------"""
        ...


# endregion-------------------------------------------------------------------------
