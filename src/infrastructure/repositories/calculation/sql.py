# endregion-------------------------------------------------------------------------
# region CALCULATION SQL REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from sqlalchemy import select

from domain.calculator.entity import CalculatorEntity

from domain.calculator.value_objects import CalculatorExpression, CalculatorResult
from domain.common.value_object import EntityCreatedAt, EntityId

from infrastructure.orm.models.calculation import CalculationModel
from infrastructure.repositories.common.sql import RepositorySQL

from lib.dt import convert_datetime_to_ms

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositorySQL(
    CalculationRepositoryBase,
    RepositorySQL[
        CalculatorEntity,
        CalculationModel,
    ],
):
    async def save_one(self, calculator: CalculatorEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculator.
        -------------------------------------------------------------------------"""
        async with self.session_maker() as session:
            model = self.to_model(calculator)

            session.add(model)
            await session.commit()

    async def get_many(self) -> list[CalculatorEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        statement = select(CalculationModel)

        async with self.session_maker() as session:
            models = await session.scalars(statement)

            return [self.to_domain(m) for m in models]

    def to_domain(self, model: CalculationModel) -> CalculatorEntity:
        return CalculatorEntity(
            calculation_id=EntityId(str(model.calculation_id)),
            result=CalculatorResult(model.result),
            expression=CalculatorExpression(model.expression),
            created_at=EntityCreatedAt(convert_datetime_to_ms(model.created_at)),
        )

    def to_model(self, entity: CalculatorEntity) -> CalculationModel:
        return CalculationModel(
            calculation_id=entity.calculation_id,
            result=entity.result,
            expression=entity.expression,
            created_at=entity.created_at.as_datetime(),
        )


# endregion-------------------------------------------------------------------------
