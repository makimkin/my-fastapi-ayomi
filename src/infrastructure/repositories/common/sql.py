# endregion-------------------------------------------------------------------------
# region SQL REPOSITORY
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from infrastructure.orm.models.base import ModelBase

from domain.common.entity import EntityBase

from .base import RepositoryBase

logger = logging.getLogger("app")


@dataclass
class RepositorySQL[E: EntityBase, M: ModelBase](RepositoryBase, ABC):
    session_maker: async_sessionmaker[AsyncSession]

    @abstractmethod
    def to_domain(self, model: M) -> E: ...

    @abstractmethod
    def to_model(self, entity: E) -> M: ...

    async def check_health(self) -> bool:
        statement = select(1)

        try:
            async with self.session_maker() as session:
                await session.execute(statement)

                return True
        except Exception as e:
            logger.error("SQL health check failed", exc_info=e)
            return False


# endregion-------------------------------------------------------------------------
