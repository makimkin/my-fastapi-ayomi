# endregion-------------------------------------------------------------------------
# region BUFFER CSV BUILDER CLASS
# ----------------------------------------------------------------------------------
import logging
import csv
import io

from dataclasses import dataclass
from abc import ABC

from .base import CSVBuilderBase

logger = logging.getLogger("app")


@dataclass
class CSVBuilderBuffer[T](CSVBuilderBase[T], ABC):
    async def build(self, items: list[T]) -> str:
        """-------------------------------------------------------------------------
        Compute the expression and return the result.
        -------------------------------------------------------------------------"""
        rows = [self.item_to_row(item) for item in items]

        if self.headers is not None:
            rows.insert(0, self.headers)

        with io.StringIO() as o:
            csv_writer = csv.writer(o)
            csv_writer.writerows(rows)

            return o.getvalue()


# endregion-------------------------------------------------------------------------
