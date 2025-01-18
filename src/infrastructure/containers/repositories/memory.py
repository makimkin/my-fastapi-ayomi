# endregion-------------------------------------------------------------------------
# region MEMORY REPOSITORIES CONTAINER
# ----------------------------------------------------------------------------------
from dishka import Scope, provide

# fmt: off
from infrastructure.repositories.calculation.base import CalculationRepositoryBase
from infrastructure.repositories.calculation.memory import CalculationRepositoryMemory
# fmt: on


class MemoryRepositoriesContainer:
    @provide(scope=Scope.APP)
    def get_calculations_repository(self) -> CalculationRepositoryBase:
        return CalculationRepositoryMemory()


# endregion-------------------------------------------------------------------------
