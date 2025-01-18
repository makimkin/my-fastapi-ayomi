# endregion-------------------------------------------------------------------------
# region CALCULATION MONGO REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from domain.calculation.entity import CalculationEntity

from infrastructure.repositories.common.mongo import RepositoryMongo

from .base import CalculationRepositoryBase


@dataclass
class CalculationRepositoryMongo(
    CalculationRepositoryBase,
    RepositoryMongo[CalculationEntity],
):
    async def save_one(self, calculator: CalculationEntity) -> None:
        """-------------------------------------------------------------------------
        Save a calculator.
        -------------------------------------------------------------------------"""
        await self.collection.insert_one(self.to_document(calculator))

    async def get_many(self) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        return [
            self.to_domain(document) async for document in self.collection.find()
        ]

    def to_domain(self, document: dict) -> CalculationEntity:
        return CalculationEntity.from_dict(document)

    def to_document(self, entity: CalculationEntity) -> dict:
        return entity.to_dict()


# endregion-------------------------------------------------------------------------
