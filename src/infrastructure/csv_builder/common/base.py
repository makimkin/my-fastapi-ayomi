# endregion-------------------------------------------------------------------------
# region BASE CSV BUILDER CLASS
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from infrastructure.common.base import InfrastructureBase

logger = logging.getLogger("app")


@dataclass
class CSVBuilderBase[I](InfrastructureBase, ABC):
    @abstractmethod
    async def build(self, items: list[I]) -> str:
        """-------------------------------------------------------------------------
        Compute the expression and return the result.
        -------------------------------------------------------------------------"""
        ...

    def item_to_row(self, item: I) -> list[str]:
        """-------------------------------------------------------------------------
        Convert the row to a list of strings.
        -------------------------------------------------------------------------"""
        return [str(i) for i in self._item_to_row(item)]

    @abstractmethod
    def _item_to_row(self, item: I) -> list[Any]:
        """-------------------------------------------------------------------------
        Convert the input data to a row.
        -------------------------------------------------------------------------"""
        ...

    @property
    @abstractmethod
    def headers(self) -> list[str] | None:
        """-------------------------------------------------------------------------
        Return the headers of the CSV.
        -------------------------------------------------------------------------"""
        ...


# endregion-------------------------------------------------------------------------
