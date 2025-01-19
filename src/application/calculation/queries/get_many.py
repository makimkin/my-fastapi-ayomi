# endregion-------------------------------------------------------------------------
# region CALCULATION GET MANY QUERY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from application.common.query import QueryPagingBase, QueryHandlerBase

from domain.calculation.entity import CalculationEntity

from infrastructure.repositories.calculation.base import CalculationRepositoryBase


@dataclass(frozen=True)
class CalculationGetManyQuery(QueryPagingBase):
    pass


@dataclass(frozen=True)
class CalculationGetManyQueryHandler(
    QueryHandlerBase[CalculationGetManyQuery, list[CalculationEntity]]
):
    calculations_repository: CalculationRepositoryBase

    async def _handle(
        self, query: CalculationGetManyQuery
    ) -> list[CalculationEntity]:
        return await self.calculations_repository.get_many(
            offset=query.offset,
            limit=query.limit,
        )


# endregion-------------------------------------------------------------------------
