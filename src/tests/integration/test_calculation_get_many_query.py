# endregion-------------------------------------------------------------------------
# region CALCULATION GET MANY QUERY TESTS
# ----------------------------------------------------------------------------------
import pytest

from application.calculation.commands import CalculationComputeCommand
from application.calculation.queries import CalculationGetManyQuery

from domain.calculation.entity import CalculationEntity
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
    Test that the CalculationGetManyQueryHandler returns a list of CalculationEntity
    instances when the query is successful.
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


@pytest.mark.asyncio
async def test_calculation_get_many_query_success_with_limit_and_offset(
    dispatcher: Dispatcher,
    calculations_repository: CalculationRepositoryMemory,
):
    """-----------------------------------------------------------------------------
    Test that the CalculationGetManyQueryHandler returns a list of CalculationEntity
    instances when the query is successful with limit and offset.
    -----------------------------------------------------------------------------"""
    # fmt: off
    compute_command_1 = CalculationComputeCommand(expression="2 2 +")
    compute_command_2 = CalculationComputeCommand(expression="2 2 -")
    compute_command_3 = CalculationComputeCommand(expression="2 2 *")
    compute_command_4 = CalculationComputeCommand(expression="2 2 /")
    compute_command_5 = CalculationComputeCommand(expression="3 3 +")
    compute_command_6 = CalculationComputeCommand(expression="3 3 -")
    compute_command_7 = CalculationComputeCommand(expression="3 3 *")
    compute_command_8 = CalculationComputeCommand(expression="3 3 /")

    calculation_1: CalculationEntity = await dispatcher.handle_command(compute_command_1)
    calculation_2: CalculationEntity = await dispatcher.handle_command(compute_command_2)
    calculation_3: CalculationEntity = await dispatcher.handle_command(compute_command_3)
    calculation_4: CalculationEntity = await dispatcher.handle_command(compute_command_4)
    calculation_5: CalculationEntity = await dispatcher.handle_command(compute_command_5)
    calculation_6: CalculationEntity = await dispatcher.handle_command(compute_command_6)
    calculation_7: CalculationEntity = await dispatcher.handle_command(compute_command_7)
    calculation_8: CalculationEntity = await dispatcher.handle_command(compute_command_8)

    assert len(calculations_repository.saved) == 8

    # test 1️⃣
    get_many_query_1 = CalculationGetManyQuery(limit=3)
    get_many_result_1 = await dispatcher.handle_query(get_many_query_1)
    assert len(get_many_result_1) == 3

    assert any(calculation.calculation_id == calculation_1.calculation_id for calculation in get_many_result_1)
    assert any(calculation.calculation_id == calculation_2.calculation_id for calculation in get_many_result_1)
    assert any(calculation.calculation_id == calculation_3.calculation_id for calculation in get_many_result_1)

    # test 2️⃣
    get_many_query_2 = CalculationGetManyQuery(limit=3, offset=3)
    get_many_result_2 = await dispatcher.handle_query(get_many_query_2)
    assert len(get_many_result_2) == 3

    assert any(calculation.calculation_id == calculation_4.calculation_id for calculation in get_many_result_2)
    assert any(calculation.calculation_id == calculation_5.calculation_id for calculation in get_many_result_2)
    assert any(calculation.calculation_id == calculation_6.calculation_id for calculation in get_many_result_2)

    # test 3️⃣
    get_many_query_3 = CalculationGetManyQuery(limit=8)
    get_many_result_3 = await dispatcher.handle_query(get_many_query_3)

    assert len(get_many_result_3) == 8

    assert any(calculation.calculation_id == calculation_1.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_2.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_3.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_4.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_5.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_6.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_7.calculation_id for calculation in get_many_result_3)
    assert any(calculation.calculation_id == calculation_8.calculation_id for calculation in get_many_result_3)

    # test 4️⃣
    get_many_query_4 = CalculationGetManyQuery(limit=10, offset=8)
    get_many_result_4 = await dispatcher.handle_query(get_many_query_4)

    assert len(get_many_result_4) == 0

    # test 5️⃣
    get_many_query_5 = CalculationGetManyQuery(limit=10, offset=10)
    get_many_result_5 = await dispatcher.handle_query(get_many_query_5)

    assert len(get_many_result_5) == 0

    # test 6️⃣
    get_many_query_6 = CalculationGetManyQuery(limit=10, offset=0)
    get_many_result_6 = await dispatcher.handle_query(get_many_query_6)

    assert len(get_many_result_6) == 8

    assert any(calculation.calculation_id == calculation_1.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_2.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_3.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_4.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_5.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_6.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_7.calculation_id for calculation in get_many_result_6)
    assert any(calculation.calculation_id == calculation_8.calculation_id for calculation in get_many_result_6)
    # fmt: on


# endregion-------------------------------------------------------------------------
