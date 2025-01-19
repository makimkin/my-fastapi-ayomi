# endregion-------------------------------------------------------------------------
# region CALCULATOR READ MANY E2E TESTS
# ----------------------------------------------------------------------------------
import pytest

from fastapi import status

from interface.api.calculator.base import CALCULATOR_ACTIONS, CALCULATOR_PREFIX
from interface.api.calculator.schemas import (
    CalculatorComputeRequest,
    #
    CalculatorReadManyParams,
    CalculatorReadManyResponse,
)

from .conftest import ContextTest


@pytest.mark.asyncio
async def test_calculator_read_many_success(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'GET' request to read many calculations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression_1 = "3 4 +"
    expression_2 = "3 4 -"
    expression_3 = "3 4 *"

    calculator_compute_request_1 = CalculatorComputeRequest(expression=expression_1)
    calculator_compute_request_2 = CalculatorComputeRequest(expression=expression_2)
    calculator_compute_request_3 = CalculatorComputeRequest(expression=expression_3)

    calculator_compute_response_1 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_1.model_dump())
    calculator_compute_response_2 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_2.model_dump())
    calculator_compute_response_3 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_3.model_dump())

    assert calculator_compute_response_1.status_code == status.HTTP_200_OK, calculator_compute_response_1.text
    assert calculator_compute_response_2.status_code == status.HTTP_200_OK, calculator_compute_response_2.text
    assert calculator_compute_response_3.status_code == status.HTTP_200_OK, calculator_compute_response_3.text

    calculator_read_many_request = CalculatorReadManyParams()
    calculator_read_many_response = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request.model_dump(exclude_none=True))
    assert calculator_read_many_response.status_code == status.HTTP_200_OK, calculator_read_many_response.text

    calculator_read_many_json, text = calculator_read_many_response.json(), calculator_read_many_response.text
    assert "items" in calculator_read_many_json, text
    assert "limit" in calculator_read_many_json, text
    assert "offset" in calculator_read_many_json, text

    calculator_read_many_data = CalculatorReadManyResponse(**calculator_read_many_json)
    assert calculator_read_many_data.limit is None, text
    assert calculator_read_many_data.offset == 0, text

    assert len(calculator_read_many_data.items) == 3, text
    assert any(item.expression == expression_1 for item in calculator_read_many_data.items), text
    assert any(item.expression == expression_2 for item in calculator_read_many_data.items), text
    assert any(item.expression == expression_3 for item in calculator_read_many_data.items), text
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_read_many_success_with_limit_and_offset(
    context: ContextTest,
):
    """-----------------------------------------------------------------------------
    Test: 'GET' request to read many calculations with limit and offset.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression_1 = "3 4 +"
    expression_2 = "3 4 -"
    expression_3 = "3 4 *"
    expression_4 = "3 4 /"
    expression_5 = "4 5 +"
    expression_6 = "4 5 -"
    expression_7 = "4 5 *"
    expression_8 = "4 5 /"

    calculator_compute_request_1 = CalculatorComputeRequest(expression=expression_1)
    calculator_compute_request_2 = CalculatorComputeRequest(expression=expression_2)
    calculator_compute_request_3 = CalculatorComputeRequest(expression=expression_3)
    calculator_compute_request_4 = CalculatorComputeRequest(expression=expression_4)
    calculator_compute_request_5 = CalculatorComputeRequest(expression=expression_5)
    calculator_compute_request_6 = CalculatorComputeRequest(expression=expression_6)
    calculator_compute_request_7 = CalculatorComputeRequest(expression=expression_7)
    calculator_compute_request_8 = CalculatorComputeRequest(expression=expression_8)

    calculator_compute_response_1 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_1.model_dump())
    calculator_compute_response_2 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_2.model_dump())
    calculator_compute_response_3 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_3.model_dump())
    calculator_compute_response_4 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_4.model_dump())
    calculator_compute_response_5 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_5.model_dump())
    calculator_compute_response_6 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_6.model_dump())
    calculator_compute_response_7 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_7.model_dump())
    calculator_compute_response_8 = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request_8.model_dump())

    assert calculator_compute_response_1.status_code == status.HTTP_200_OK, calculator_compute_response_1.text
    assert calculator_compute_response_2.status_code == status.HTTP_200_OK, calculator_compute_response_2.text
    assert calculator_compute_response_3.status_code == status.HTTP_200_OK, calculator_compute_response_3.text
    assert calculator_compute_response_4.status_code == status.HTTP_200_OK, calculator_compute_response_4.text
    assert calculator_compute_response_5.status_code == status.HTTP_200_OK, calculator_compute_response_5.text
    assert calculator_compute_response_6.status_code == status.HTTP_200_OK, calculator_compute_response_6.text
    assert calculator_compute_response_7.status_code == status.HTTP_200_OK, calculator_compute_response_7.text
    assert calculator_compute_response_8.status_code == status.HTTP_200_OK, calculator_compute_response_8.text

    # test 1️⃣
    calculator_read_many_request_1 = CalculatorReadManyParams(limit=0, offset=0)
    calculator_read_many_response_1 = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request_1.model_dump(exclude_none=True))
    assert calculator_read_many_response_1.status_code == status.HTTP_200_OK, calculator_read_many_response_1.text

    calculator_read_many_json_1, text_1 = calculator_read_many_response_1.json(), calculator_read_many_response_1.text

    calculator_read_many_data_1 = CalculatorReadManyResponse(**calculator_read_many_json_1)
    assert calculator_read_many_data_1.limit == 0, text_1
    assert calculator_read_many_data_1.offset == 0, text_1

    assert len(calculator_read_many_data_1.items) == 0, text_1

    # test 2️⃣
    calculator_read_many_request_2 = CalculatorReadManyParams(limit=3, offset=0)
    calculator_read_many_response_2 = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request_2.model_dump(exclude_none=True))
    assert calculator_read_many_response_2.status_code == status.HTTP_200_OK, calculator_read_many_response_2.text

    calculator_read_many_json_2, text_2 = calculator_read_many_response_2.json(), calculator_read_many_response_2.text

    calculator_read_many_data_2 = CalculatorReadManyResponse(**calculator_read_many_json_2)
    assert calculator_read_many_data_2.limit == 3, text_2
    assert calculator_read_many_data_2.offset == 0, text_2

    assert len(calculator_read_many_data_2.items) == 3, text_2
    assert any(item.expression == expression_1 for item in calculator_read_many_data_2.items), text_2
    assert any(item.expression == expression_2 for item in calculator_read_many_data_2.items), text_2
    assert any(item.expression == expression_3 for item in calculator_read_many_data_2.items), text_2
    assert all(item.expression != expression_4 for item in calculator_read_many_data_2.items), text_2
    assert all(item.expression != expression_5 for item in calculator_read_many_data_2.items), text_2
    assert all(item.expression != expression_6 for item in calculator_read_many_data_2.items), text_2
    assert all(item.expression != expression_7 for item in calculator_read_many_data_2.items), text_2
    assert all(item.expression != expression_8 for item in calculator_read_many_data_2.items), text_2

    # test 3️⃣
    calculator_read_many_request_3 = CalculatorReadManyParams(limit=3, offset=3)
    calculator_read_many_response_3 = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request_3.model_dump(exclude_none=True))
    assert calculator_read_many_response_3.status_code == status.HTTP_200_OK, calculator_read_many_response_3.text

    calculator_read_many_json_3, text_3 = calculator_read_many_response_3.json(), calculator_read_many_response_3.text

    calculator_read_many_data_3 = CalculatorReadManyResponse(**calculator_read_many_json_3)
    assert calculator_read_many_data_3.limit == 3, text_3
    assert calculator_read_many_data_3.offset == 3, text_3

    assert len(calculator_read_many_data_3.items) == 3, text_3
    assert all(item.expression != expression_1 for item in calculator_read_many_data_3.items), text_3
    assert all(item.expression != expression_2 for item in calculator_read_many_data_3.items), text_3
    assert all(item.expression != expression_3 for item in calculator_read_many_data_3.items), text_3
    assert any(item.expression == expression_4 for item in calculator_read_many_data_3.items), text_3
    assert any(item.expression == expression_5 for item in calculator_read_many_data_3.items), text_3
    assert any(item.expression == expression_6 for item in calculator_read_many_data_3.items), text_3
    assert all(item.expression != expression_7 for item in calculator_read_many_data_3.items), text_3
    assert all(item.expression != expression_8 for item in calculator_read_many_data_3.items), text_3

    # test 4️⃣
    calculator_read_many_request_4 = CalculatorReadManyParams(limit=8, offset=0)
    calculator_read_many_response_4 = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request_4.model_dump(exclude_none=True))
    assert calculator_read_many_response_4.status_code == status.HTTP_200_OK, calculator_read_many_response_4.text

    calculator_read_many_json_4, text_4 = calculator_read_many_response_4.json(), calculator_read_many_response_4.text

    calculator_read_many_data_4 = CalculatorReadManyResponse(**calculator_read_many_json_4)
    assert calculator_read_many_data_4.limit == 8, text_4
    assert calculator_read_many_data_4.offset == 0, text_4

    assert len(calculator_read_many_data_4.items) == 8, text_4
    assert any(item.expression == expression_1 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_2 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_3 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_4 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_5 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_6 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_7 for item in calculator_read_many_data_4.items), text_4
    assert any(item.expression == expression_8 for item in calculator_read_many_data_4.items), text_4

    # test 5️⃣
    calculator_read_many_request_5 = CalculatorReadManyParams(limit=10, offset=8)
    calculator_read_many_response_5 = await context.get(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.READ_MANY}", params=calculator_read_many_request_5.model_dump(exclude_none=True))
    assert calculator_read_many_response_5.status_code == status.HTTP_200_OK, calculator_read_many_response_5.text

    calculator_read_many_json_5, text_5 = calculator_read_many_response_5.json(), calculator_read_many_response_5.text

    calculator_read_many_data_5 = CalculatorReadManyResponse(**calculator_read_many_json_5)
    assert calculator_read_many_data_5.limit == 10, text_5
    assert calculator_read_many_data_5.offset == 8, text_5

    assert len(calculator_read_many_data_5.items) == 0, text_5
    # fmt: on


# endregion-------------------------------------------------------------------------
