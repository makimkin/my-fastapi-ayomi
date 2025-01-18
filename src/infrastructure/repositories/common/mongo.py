# endregion-------------------------------------------------------------------------
# region MONGO REPOSITORY
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorCollection

from domain.common.entity import EntityBase

from .base import RepositoryBase

logger = logging.getLogger("app")


@dataclass
class RepositoryMongo[E: EntityBase](RepositoryBase, ABC):
    collection: AsyncIOMotorCollection

    @abstractmethod
    def to_domain(self, document: dict) -> E: ...

    @abstractmethod
    def to_document(self, entity: E) -> dict: ...

    async def check_health(self) -> bool:
        try:
            await self.collection.find_one({})
            return True
        except Exception as e:
            logger.error("MongoDB health check failed", exc_info=e)
            return False


# endregion-------------------------------------------------------------------------
