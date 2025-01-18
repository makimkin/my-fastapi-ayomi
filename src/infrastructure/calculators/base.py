# endregion-------------------------------------------------------------------------
# region BASE CALCULATOR CLASS
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass

from infrastructure.common.base import InfrastructureBase

logger = logging.getLogger("app")


@dataclass
class CalculatorBase(InfrastructureBase, ABC):
    @abstractmethod
    async def compute(self, expression: str) -> float:
        """-------------------------------------------------------------------------
        Compute the expression and return the result.
        -------------------------------------------------------------------------"""
        ...

    async def check_health(self) -> bool:
        return True


# endregion-------------------------------------------------------------------------
