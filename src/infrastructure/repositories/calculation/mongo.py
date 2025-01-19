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
        document = self.to_document(calculator)

        await self.collection.insert_one(document)

    async def get_many(
        self,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[CalculationEntity]:
        """-------------------------------------------------------------------------
        Get all calculators.
        -------------------------------------------------------------------------"""
        items = await self.collection.find().skip(offset).to_list(length=limit)

        return [self.to_domain(document) for document in items]

    def to_domain(self, document: dict) -> CalculationEntity:
        return CalculationEntity.from_dict(document)

    def to_document(self, entity: CalculationEntity) -> dict:
        return entity.to_dict()


# endregion-------------------------------------------------------------------------
