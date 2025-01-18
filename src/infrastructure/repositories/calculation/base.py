# endregion-------------------------------------------------------------------------
# region CALCULATION BASE REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.calculation.entity import CalculationEntity


@dataclass
class CalculationRepositoryBase(ABC):
    @abstractmethod
    async def save_one(self, calculation: CalculationEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculation.
        -------------------------------------------------------------------------"""
        ...

    @abstractmethod
    async def get_many(self) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculations.
        -------------------------------------------------------------------------"""
        ...


# endregion-------------------------------------------------------------------------
