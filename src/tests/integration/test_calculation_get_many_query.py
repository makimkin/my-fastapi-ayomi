# endregion-------------------------------------------------------------------------
# region CALCULATION GET MANY QUERY TESTS
# ----------------------------------------------------------------------------------
import pytest

from application.calculation.commands import CalculationComputeCommand
from application.calculation.queries import CalculationGetManyQuery

from infrastructure.dispatchers.dispatcher import Dispatcher
from infrastructure.repositories.calculation.memory import (
    CalculationRepositoryMemory,
)


@pytest.mark.asyncio
async def test_calculation_get_many_query_success(
    dispatcher: Dispatcher,
    calculations_repository: CalculationRepositoryMemory,
):
    """-----------------------------------------------------------------------------
    Test clicker cache leader clicks method.
    -----------------------------------------------------------------------------"""
    # fmt: off
    compute_command_1 = CalculationComputeCommand(expression="2 2 +")
    compute_command_2 = CalculationComputeCommand(expression="2 2 -")
    compute_command_3 = CalculationComputeCommand(expression="2 2 *")

    await dispatcher.handle_command(compute_command_1)
    await dispatcher.handle_command(compute_command_2)
    await dispatcher.handle_command(compute_command_3)

    assert len(calculations_repository.saved) == 3

    get_many_query = CalculationGetManyQuery()
    get_many_result = await dispatcher.handle_query(get_many_query)
    assert len(get_many_result) == 3
    # fmt: on


# endregion-------------------------------------------------------------------------
