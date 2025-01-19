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


# endregion-------------------------------------------------------------------------
