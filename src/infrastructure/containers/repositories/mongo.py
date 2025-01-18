# endregion-------------------------------------------------------------------------
# region MONGO REPOSITORIES CONTAINER
# ----------------------------------------------------------------------------------
from dishka import provide, Scope

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


from infrastructure.repositories.calculation.base import CalculationRepositoryBase
from infrastructure.repositories.calculation.mongo import CalculationRepositoryMongo
from settings.config import Config


class MongoRepositoriesContainer:
    @provide(scope=Scope.APP)
    def get_mongo_client(self, config: Config) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(config.MONGO_URI)

    @provide(scope=Scope.APP)
    def get_mongo_db(
        self,
        config: Config,
        client: AsyncIOMotorClient,
    ) -> AsyncIOMotorDatabase:
        return client[config.MONGO_DB]

    @provide(scope=Scope.APP)
    def get_calculations_repository(
        self,
        config: Config,
        mongo_db: AsyncIOMotorDatabase,
    ) -> CalculationRepositoryBase:
        return CalculationRepositoryMongo(
            collection=mongo_db[config.MONGO_CALCULATIONS_COLLECTION_NAME]
        )


# endregion-------------------------------------------------------------------------
