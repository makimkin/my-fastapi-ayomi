# endregion-------------------------------------------------------------------------
# region CONTAINER MOCK
# ----------------------------------------------------------------------------------
from .repositories.memory import MemoryRepositoriesContainer
from .base import ContainerBase


class ContainerMock(
    ContainerBase,
    MemoryRepositoriesContainer,
): ...


# endregion-------------------------------------------------------------------------
