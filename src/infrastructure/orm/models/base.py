# endregion-------------------------------------------------------------------------
# region BASE MODELS
# ----------------------------------------------------------------------------------
from enum import Enum

from sqlalchemy.orm import DeclarativeBase


# endregion-------------------------------------------------------------------------
# region TABLES
# ----------------------------------------------------------------------------------
class TABLES(str, Enum):
    CALCULATIONS = "calculations"

    def __str__(self) -> str:
        return self.value


# endregion-------------------------------------------------------------------------
# region ASSOCIATION TABLES
# ----------------------------------------------------------------------------------
class ASSOCIATION_TABLES(str, Enum):
    def __str__(self) -> str:
        return self.value


# endregion-------------------------------------------------------------------------
# region BASE MODEL
# ----------------------------------------------------------------------------------
class ModelBase(DeclarativeBase):
    __allow_unmapped__ = True


# endregion-------------------------------------------------------------------------
