# endregion-------------------------------------------------------------------------
# region CONTAINER BASE
# ----------------------------------------------------------------------------------

from settings.config import Config

from dishka import Scope, Provider, provide

from application.calculation.commands import (
    CalculationComputeCommandHandler,
    CalculationComputeCommand,
    #
)
from application.calculation.queries.get_many import (
    CalculationGetManyQueryHandler,
    CalculationGetManyQuery,
    #
)

from infrastructure.repositories.calculation.base import CalculationRepositoryBase

from ..calculators.rpn import CalculatorRPN
from ..calculators.base import CalculatorBase
from ..dispatchers.dispatcher import Dispatcher


class ContainerBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()

    @provide(scope=Scope.APP)
    def get_calculator(self) -> CalculatorBase:
        return CalculatorRPN()

    @provide(scope=Scope.APP)
    def get_dispatcher(
        self,
        calculator: CalculatorBase,
        calculations_repository: CalculationRepositoryBase,
    ) -> Dispatcher:
        dispatcher = Dispatcher()

        # COMMANDS
        calculation_compute_command_handler = CalculationComputeCommandHandler(
            calculations_repository=calculations_repository,
            calculator=calculator,
        )

        dispatcher.register_command(
            CalculationComputeCommand,
            calculation_compute_command_handler,
        )

        # QUERIES
        calculation_get_many_query_handler = CalculationGetManyQueryHandler(
            calculations_repository=calculations_repository,
        )

        dispatcher.register_query(
            CalculationGetManyQuery,
            calculation_get_many_query_handler,
        )

        return dispatcher


# endregion-------------------------------------------------------------------------
