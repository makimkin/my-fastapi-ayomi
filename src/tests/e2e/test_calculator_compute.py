# endregion-------------------------------------------------------------------------
# region CALCULATOR COMPUTE E2E TESTS
# ----------------------------------------------------------------------------------
import pytest

from fastapi import status

from domain.calculation.exceptions import CalculationExpressionEmptyException

from infrastructure.calculators.exceptions import (
    CalculatorExpressionInvalidException,
    CalculatorDivisionByZeroException,
)

from interface.api.calculator.base import CALCULATOR_ACTIONS, CALCULATOR_PREFIX
from interface.api.calculator.schemas import (
    CalculatorComputeResponse,
    CalculatorComputeRequest,
)
from interface.api.schemas import ErrorSchema

from .conftest import ContextTest


@pytest.mark.asyncio
async def test_calculator_compute_success(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'POST' request to compute a simple expression.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression = "3 4 +"

    calculator_compute_request = CalculatorComputeRequest(expression=expression)
    calculator_compute_response = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request.model_dump())
    assert calculator_compute_response.status_code == status.HTTP_200_OK, calculator_compute_response.text

    calculator_compute_json, text = calculator_compute_response.json(), calculator_compute_response.text
    assert "expression" in calculator_compute_json, text
    assert "result" in calculator_compute_json, text

    calculator_compute_data = CalculatorComputeResponse(**calculator_compute_json)
    assert calculator_compute_data.expression == expression, text
    assert calculator_compute_data.result == 7, text
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_compute_success_floating_problem(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'POST' request to compute a simple expression with floating point numbers.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression = "0.1 0.2 +"

    calculator_compute_request = CalculatorComputeRequest(expression=expression)
    calculator_compute_response = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request.model_dump())
    assert calculator_compute_response.status_code == status.HTTP_200_OK, calculator_compute_response.text

    calculator_compute_json, text = calculator_compute_response.json(), calculator_compute_response.text
    assert "expression" in calculator_compute_json, text
    assert "result" in calculator_compute_json, text

    calculator_compute_data = CalculatorComputeResponse(**calculator_compute_json)
    assert calculator_compute_data.expression == expression, text
    assert calculator_compute_data.result == 0.3, text
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_compute_error_invalid_expression(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'POST' request to compute an invalid expression.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression = "3 4 + +"

    calculator_compute_request = CalculatorComputeRequest(expression=expression)
    calculator_compute_response = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request.model_dump())
    assert calculator_compute_response.status_code == status.HTTP_400_BAD_REQUEST, calculator_compute_response.text

    calculator_compute_json, text = calculator_compute_response.json(), calculator_compute_response.text
    assert "detail" in calculator_compute_json, text
    assert "name" in calculator_compute_json["detail"], text
    assert "error" in calculator_compute_json["detail"], text


    calculator_compute_error = ErrorSchema(**calculator_compute_json)
    assert calculator_compute_error.detail.name == CalculatorExpressionInvalidException.__name__, text
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_compute_error_division_by_zero(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'POST' request to compute an expression with division by zero.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression = "3 0 /"

    calculator_compute_request = CalculatorComputeRequest(expression=expression)
    calculator_compute_response = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request.model_dump())
    assert calculator_compute_response.status_code == status.HTTP_400_BAD_REQUEST, calculator_compute_response.text

    calculator_compute_json, text = calculator_compute_response.json(), calculator_compute_response.text
    assert "detail" in calculator_compute_json, text
    assert "name" in calculator_compute_json["detail"], text
    assert "error" in calculator_compute_json["detail"], text

    calculator_compute_error = ErrorSchema(**calculator_compute_json)
    assert calculator_compute_error.detail.name == CalculatorDivisionByZeroException.__name__, text
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_compute_error_empty_expression(context: ContextTest):
    """-----------------------------------------------------------------------------
    Test: 'POST' request to compute an empty expression.
    -----------------------------------------------------------------------------"""
    # fmt: off
    expression = ""

    calculator_compute_request = CalculatorComputeRequest(expression=expression)
    calculator_compute_response = await context.post(f"/v1{CALCULATOR_PREFIX}{CALCULATOR_ACTIONS.COMPUTE}", json=calculator_compute_request.model_dump())
    assert calculator_compute_response.status_code == status.HTTP_400_BAD_REQUEST, calculator_compute_response.text

    calculator_compute_json, text = calculator_compute_response.json(), calculator_compute_response.text
    assert "detail" in calculator_compute_json, text
    assert "name" in calculator_compute_json["detail"], text
    assert "error" in calculator_compute_json["detail"], text

    calculator_compute_error = ErrorSchema(**calculator_compute_json)
    assert calculator_compute_error.detail.name == CalculationExpressionEmptyException.__name__, text
    # fmt: on


# endregion-------------------------------------------------------------------------
