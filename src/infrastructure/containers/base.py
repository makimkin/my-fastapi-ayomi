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
    ) -> Dispatcher:
        dispatcher = Dispatcher()

        # COMMANDS
        calculator_compute_command_handler = CalculationComputeCommandHandler(
            calculator=calculator,
        )

        dispatcher.register_command(
            CalculationComputeCommand,
            calculator_compute_command_handler,
        )

        return dispatcher


# endregion-------------------------------------------------------------------------
