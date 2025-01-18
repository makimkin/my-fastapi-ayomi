# endregion-------------------------------------------------------------------------
# region SQL REPOSITORIES CONTAINER
# ----------------------------------------------------------------------------------
from dishka import provide, Scope

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from infrastructure.repositories.calculation.base import CalculationRepositoryBase
from infrastructure.repositories.calculation.sql import CalculationRepositorySQL

from settings.config import Config


class SQLRepositoriesContainer:
    @provide(scope=Scope.APP)
    def get_sql_session_maker(
        self,
        config: Config,
    ) -> async_sessionmaker[AsyncSession]:
        engine = create_async_engine(config.SQL_URI, echo=True, future=True)

        return async_sessionmaker(
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
            bind=engine,
        )

    @provide(scope=Scope.APP)
    def get_calculations_repository(
        self,
        session_maker: async_sessionmaker[AsyncSession],
    ) -> CalculationRepositoryBase:
        return CalculationRepositorySQL(session_maker=session_maker)


# endregion-------------------------------------------------------------------------
