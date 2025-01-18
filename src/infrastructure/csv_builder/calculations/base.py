# endregion-------------------------------------------------------------------------
# region CALCULATIONS BASE CSV BUILDER CLASS
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from typing import Any
from abc import ABC

from domain.calculation.entity import CalculationEntity

from ..common.base import CSVBuilderBase

logger = logging.getLogger("app")


@dataclass
class CalculationsCSVBuilderBase(CSVBuilderBase[CalculationEntity], ABC):
    def _item_to_row(self, data: CalculationEntity) -> list[Any]:
        """-------------------------------------------------------------------------
        Convert the input data to a row.
        -------------------------------------------------------------------------"""
        return [
            data.calculation_id.as_raw(),
            data.expression.as_raw(),
            "" if data.result is None else float(data.result.as_raw()),
            data.created_at.as_raw(),
        ]

    @property
    def headers(self) -> list[str] | None:
        """-------------------------------------------------------------------------
        Return the headers of the CSV.
        -------------------------------------------------------------------------"""
        return [
            "ID",
            "Expression",
            "Result",
            "Created at",
        ]


# endregion-------------------------------------------------------------------------
