# endregion-------------------------------------------------------------------------
# region CONFTEST
# ----------------------------------------------------------------------------------
import pytest_asyncio
import pytest

from dishka import AsyncContainer, make_async_container

from infrastructure.repositories.calculation.base import CalculationRepositoryBase
from infrastructure.dispatchers.dispatcher import Dispatcher
from infrastructure.containers.mock import ContainerMock

from settings.config import Config


@pytest.fixture(scope="function")
def container() -> AsyncContainer:
    return make_async_container(ContainerMock())


@pytest_asyncio.fixture(scope="function")
async def dispatcher(container: AsyncContainer) -> Dispatcher:
    return await container.get(Dispatcher)


@pytest_asyncio.fixture(scope="function")
async def config(container: AsyncContainer) -> Config:
    return await container.get(Config)


@pytest_asyncio.fixture(scope="function")
async def calculations_repository(container: AsyncContainer):
    return await container.get(CalculationRepositoryBase)


# endregion-------------------------------------------------------------------------
