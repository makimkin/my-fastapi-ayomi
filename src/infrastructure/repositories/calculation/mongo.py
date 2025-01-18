# endregion-------------------------------------------------------------------------
# region CALCULATION MONGO REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.calculator.entity import CalculatorEntity

from infrastructure.repositories.common.mongo import RepositoryMongo

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositoryMongo(
    CalculationRepositoryBase,
    RepositoryMongo[CalculatorEntity],
):
    async def save_one(self, calculator: CalculatorEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculator.
        -------------------------------------------------------------------------"""
        await self.collection.insert_one(self.to_document(calculator))

    async def get_many(self) -> list[CalculatorEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        return [
            self.to_domain(document) async for document in self.collection.find()
        ]

    def to_domain(self, document: dict) -> CalculatorEntity:
        return CalculatorEntity.from_dict(document)

    def to_document(self, entity: CalculatorEntity) -> dict:
        return entity.to_dict()


# endregion-------------------------------------------------------------------------
