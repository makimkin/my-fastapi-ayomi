# endregion-------------------------------------------------------------------------
# region CONTAINER BASE
# ----------------------------------------------------------------------------------

from settings.config import Config

from dishka import Scope, Provider, provide

from application.calculation.commands import (
    CalculationComputeCommandHandler,
    CalculationComputeCommand,
    #
    CalculationGenerateCSVCommandHandler,
    CalculationGenerateCSVCommand,
)
from application.calculation.queries import (
    CalculationGetManyQueryHandler,
    CalculationGetManyQuery,
    #
)

# fmt: off
from infrastructure.repositories.calculation.base import CalculationRepositoryBase
from infrastructure.csv_builder.calculations.base import CalculationsCSVBuilderBase
from infrastructure.csv_builder.calculations.buffer import CalculationsCSVBuilderBuffer
# fmt: on

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
    def get_calculations_csv_builder(self) -> CalculationsCSVBuilderBase:
        return CalculationsCSVBuilderBuffer()

    @provide(scope=Scope.APP)
    def get_dispatcher(
        self,
        calculator: CalculatorBase,
        calculations_repository: CalculationRepositoryBase,
        calculations_csv_builder: CalculationsCSVBuilderBase,
    ) -> Dispatcher:
        dispatcher = Dispatcher()

        # COMMANDS
        # COMPUTE
        calculation_compute_command_handler = CalculationComputeCommandHandler(
            calculations_repository=calculations_repository,
            calculator=calculator,
        )

        dispatcher.register_command(
            CalculationComputeCommand,
            calculation_compute_command_handler,
        )

        # GENERATE CSV
        calculation_generate_csv_command_handler = (
            CalculationGenerateCSVCommandHandler(
                calculations_repository=calculations_repository,
                calculations_csv_builder=calculations_csv_builder,
            )
        )

        dispatcher.register_command(
            CalculationGenerateCSVCommand,
            calculation_generate_csv_command_handler,
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
