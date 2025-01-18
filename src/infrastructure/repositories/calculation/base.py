# endregion-------------------------------------------------------------------------
# region CALCULATION BASE REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.calculator.entity import CalculatorEntity


@dataclass
class CalculationRepositoryBase(ABC):
    @abstractmethod
    async def save_one(self, calculator: CalculatorEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculator.
        -------------------------------------------------------------------------"""
        ...

    @abstractmethod
    async def get_many(self) -> list[CalculatorEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        ...


# endregion-------------------------------------------------------------------------
