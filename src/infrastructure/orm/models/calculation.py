# endregion-------------------------------------------------------------------------
# region CALCULATION MODEL
# ----------------------------------------------------------------------------------
import datetime

from decimal import Decimal

from sqlalchemy import TIMESTAMP, DECIMAL, TEXT, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import ModelBase, TABLES


class CalculationModel(ModelBase):
    """-----------------------------------------------------------------------------
    Calculation Model.
    -----------------------------------------------------------------------------"""

    __tablename__ = TABLES.CALCULATIONS

    calculation_id: Mapped[UUID] = mapped_column(UUID, primary_key=True)

    expression: Mapped[str] = mapped_column(TEXT)
    result: Mapped[Decimal | None] = mapped_column(DECIMAL)

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)


# endregion-------------------------------------------------------------------------
