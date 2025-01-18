# endregion-------------------------------------------------------------------------
# region CONTAINER APP
# ----------------------------------------------------------------------------------
from .base import ContainerBase
from .repositories.sql import SQLRepositoriesContainer


class ContainerApp(
    ContainerBase,
    SQLRepositoriesContainer,
): ...


# endregion-------------------------------------------------------------------------
