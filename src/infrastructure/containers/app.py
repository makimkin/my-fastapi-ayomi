# endregion-------------------------------------------------------------------------
# region CONTAINER APP
# ----------------------------------------------------------------------------------
from .repositories.mongo import MongoRepositoriesContainer
from .base import ContainerBase


class ContainerApp(
    ContainerBase,
    MongoRepositoriesContainer,
): ...


# endregion-------------------------------------------------------------------------
