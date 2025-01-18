# endregion-------------------------------------------------------------------------
# region BASE REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import ABC

from infrastructure.common.base import InfrastructureBase


@dataclass
class RepositoryBase(InfrastructureBase, ABC): ...


# endregion-------------------------------------------------------------------------
