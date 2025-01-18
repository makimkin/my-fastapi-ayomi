# endregion-------------------------------------------------------------------------
# region CONTAINER APP
# ----------------------------------------------------------------------------------
from .repositories.mongo import MongoRepositoriesContainer
from .repositories.sql import SQLRepositoriesContainer
from .base import ContainerBase

from settings.config import Config

config = Config()


match config.APP_DB:
    case "mongo":
        ContainerApp = type(
            "ContainerApp",
            (ContainerBase, MongoRepositoriesContainer),
            {},
        )
    case "postgres":
        ContainerApp = type(
            "ContainerApp",
            (ContainerBase, SQLRepositoriesContainer),
            {},
        )




# endregion-------------------------------------------------------------------------
