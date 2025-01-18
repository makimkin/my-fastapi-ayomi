# endregion-------------------------------------------------------------------------
# region CALCULATION SQL REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from sqlalchemy import select

from domain.calculation.value_objects import (
    CalculationExpression,
    CalculationResult,
)
from domain.common.value_object import EntityCreatedAt, EntityId
from domain.calculation.entity import CalculationEntity

from infrastructure.orm.models.calculation import CalculationModel
from infrastructure.repositories.common.sql import RepositorySQL

from lib.dt import convert_datetime_to_ms

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositorySQL(
    CalculationRepositoryBase,
    RepositorySQL[
        CalculationEntity,
        CalculationModel,
    ],
):
    async def save_one(self, calculation: CalculationEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculation.
        -------------------------------------------------------------------------"""
        async with self.session_maker() as session:
            model = self.to_model(calculation)

            session.add(model)
            await session.commit()

    async def get_many(self) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculations.
        -------------------------------------------------------------------------"""
        statement = select(CalculationModel)

        async with self.session_maker() as session:
            models = await session.scalars(statement)

            return [self.to_domain(m) for m in models]

    def to_domain(self, model: CalculationModel) -> CalculationEntity:
        return CalculationEntity(
            calculation_id=EntityId(str(model.calculation_id)),
            result=None
            if model.result is None
            else CalculationResult(model.result),
            expression=CalculationExpression(model.expression),
            created_at=EntityCreatedAt(convert_datetime_to_ms(model.created_at)),
        )

    def to_model(self, entity: CalculationEntity) -> CalculationModel:
        return CalculationModel(
            calculation_id=entity.calculation_id.as_raw(),
            result=None if entity.result is None else entity.result.as_raw(),
            expression=entity.expression.as_raw(),
            created_at=entity.created_at.as_datetime(),
        )


# endregion-------------------------------------------------------------------------
