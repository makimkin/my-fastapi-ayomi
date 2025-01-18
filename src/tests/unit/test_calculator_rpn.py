# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR TESTS
# ----------------------------------------------------------------------------------
import pytest

from domain.calculation.value_objects import CalculationExpression

from infrastructure.calculators.exceptions import CalculatorDivisionByZeroException
from infrastructure.calculators.rpn import CalculatorRPN


@pytest.mark.asyncio
async def test_calculator_rpn_success_plus_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculationExpression("3 4 +")
    assert await calculator_rpn.compute(expression_1) == 7

    expression_2 = CalculationExpression("3 4 + 5 +")
    assert await calculator_rpn.compute(expression_2) == 12

    expression_3 = CalculationExpression("3 4 + 5 + 2 +")
    assert await calculator_rpn.compute(expression_3) == 14

    expression_4 = CalculationExpression("3 4 + 5 + 2 + 1 +")
    assert await calculator_rpn.compute(expression_4) == 15

    expression_5 = CalculationExpression("3 4 + 5 + 2 + 1 + 2 +")
    assert await calculator_rpn.compute(expression_5) == 17
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_success_substract_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculationExpression("10 5 -")
    assert await calculator_rpn.compute(expression_1) == 5

    expression_2 = CalculationExpression("10 5 2 - -")
    assert await calculator_rpn.compute(expression_2) == 7

    expression_3 = CalculationExpression("10 5 2 - - 1 -")
    assert await calculator_rpn.compute(expression_3) == 6

    expression_4 = CalculationExpression("10 5 2 - - 1 - 2 -")
    assert await calculator_rpn.compute(expression_4) == 4

    expression_5 = CalculationExpression("10 5 2 - - 1 - 2 - 1 -")
    assert await calculator_rpn.compute(expression_5) == 3
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_success_multiply_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculationExpression("3 4 *")
    assert await calculator_rpn.compute(expression_1) == 12

    expression_2 = CalculationExpression("3 4 * 5 *")
    assert await calculator_rpn.compute(expression_2) == 60

    expression_3 = CalculationExpression("3 4 * 5 * 2 *")
    assert await calculator_rpn.compute(expression_3) == 120

    expression_4 = CalculationExpression("3 4 * 5 * 2 * 1 *")
    assert await calculator_rpn.compute(expression_4) == 120

    expression_5 = CalculationExpression("3 4 * 5 * 2 * 1 * 2 *")
    assert await calculator_rpn.compute(expression_5) == 240
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_success_divide_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculationExpression("8 4 /")
    assert await calculator_rpn.compute(expression_1) == 2

    expression_2 = CalculationExpression("8 4 2 / /")
    assert await calculator_rpn.compute(expression_2) == 4

    expression_3 = CalculationExpression("8 4 2 / / 2 /")
    assert await calculator_rpn.compute(expression_3) == 2

    expression_4 = CalculationExpression("8 4 2 / / 2 / 2 /")
    assert await calculator_rpn.compute(expression_4) == 1

    expression_5 = CalculationExpression("8 4 2 / / 2 / 2 / 2 /")
    assert await calculator_rpn.compute(expression_5) == 0.5
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_error_division_by_zero() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculationExpression("8 0 /")
    with pytest.raises(CalculatorDivisionByZeroException):
        await calculator_rpn.compute(expression_1)

    expression_2 = CalculationExpression("8 0 2 4 + / / ")
    with pytest.raises(CalculatorDivisionByZeroException):
        await calculator_rpn.compute(expression_2)

    expression_3 = CalculationExpression("8 0 2 4 + / / 2 /")
    with pytest.raises(CalculatorDivisionByZeroException):
        await calculator_rpn.compute(expression_3)

    expression_4 = CalculationExpression("8 0 2 4 + / / 2 / 2 /")
    with pytest.raises(CalculatorDivisionByZeroException):
        await calculator_rpn.compute(expression_4)

    expression_5 = CalculationExpression("8 0 2 4 + / / 2 / 2 / 2 /")
    with pytest.raises(CalculatorDivisionByZeroException):
        await calculator_rpn.compute(expression_5)
    # fmt: on


# endregion-------------------------------------------------------------------------
