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

    async def get_many(
        self,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculations.
        -------------------------------------------------------------------------"""
        statement = select(CalculationModel).offset(offset).limit(limit)

        async with self.session_maker() as session:
            models = await session.scalars(statement)

            return [self.to_domain(m) for m in models]

    def to_domain(self, model: CalculationModel) -> CalculationEntity:
        return CalculationEntity(
            result=None
            if model.result is None
            else CalculationResult(model.result),
            created_at=EntityCreatedAt(model.created_at),
            expression=CalculationExpression(model.expression),
            calculation_id=EntityId(str(model.calculation_id)),
        )

    def to_model(self, entity: CalculationEntity) -> CalculationModel:
        return CalculationModel(
            result=None if entity.result is None else entity.result.as_raw(),
            calculation_id=entity.calculation_id.as_raw(),
            expression=entity.expression.as_raw(),
            created_at=entity.created_at.as_raw(),
        )


# endregion-------------------------------------------------------------------------
