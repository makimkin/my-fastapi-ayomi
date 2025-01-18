# endregion-------------------------------------------------------------------------
# region CONTAINER BASE
# ----------------------------------------------------------------------------------
from settings.config import Config
from typing import AsyncIterable

from dishka import Scope, Provider, provide

from application.calculator.commands import (
    CalculatorComputeCommandHandler,
    CalculatorComputeCommand,
    #
)

# fmt: off
from ..calculators.rpn import CalculatorRPN
from ..calculators.base import CalculatorBase
from ..dispatchers.dispatcher import Dispatcher
from ..connection_manager.common.base import ConnectionManagerBase
from ..connection_manager.fastapi.concurrent import FastAPIConnectionManagerConcurrent
# fmt: on


class ContainerBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()

    @provide(scope=Scope.APP)
    async def get_connection_manager(self) -> AsyncIterable[ConnectionManagerBase]:
        connection_manager = FastAPIConnectionManagerConcurrent()

        yield connection_manager

        await connection_manager.close()

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
        calculator_compute_command_handler = CalculatorComputeCommandHandler(
            calculator=calculator,
        )

        dispatcher.register_command(
            CalculatorComputeCommand,
            calculator_compute_command_handler,
        )

        return dispatcher


# endregion-------------------------------------------------------------------------
