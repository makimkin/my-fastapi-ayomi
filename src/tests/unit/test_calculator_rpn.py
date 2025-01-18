# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR TESTS
# ----------------------------------------------------------------------------------
import pytest

from domain.calculator.value_objects import CalculatorExpression

from infrastructure.calculators.rpn import CalculatorRPN


@pytest.mark.asyncio
async def test_calculator_rpn_plus_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculatorExpression("3 4 +")
    assert await calculator_rpn.compute(expression_1) == 7

    expression_2 = CalculatorExpression("3 4 + 5 +")
    assert await calculator_rpn.compute(expression_2) == 12

    expression_3 = CalculatorExpression("3 4 + 5 + 2 +")
    assert await calculator_rpn.compute(expression_3) == 14

    expression_4 = CalculatorExpression("3 4 + 5 + 2 + 1 +")
    assert await calculator_rpn.compute(expression_4) == 15

    expression_5 = CalculatorExpression("3 4 + 5 + 2 + 1 + 2 +")
    assert await calculator_rpn.compute(expression_5) == 17
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_substract_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculatorExpression("10 5 -")
    assert await calculator_rpn.compute(expression_1) == 5

    expression_2 = CalculatorExpression("10 5 2 - -")
    assert await calculator_rpn.compute(expression_2) == 7

    expression_3 = CalculatorExpression("10 5 2 - - 1 -")
    assert await calculator_rpn.compute(expression_3) == 6

    expression_4 = CalculatorExpression("10 5 2 - - 1 - 2 -")
    assert await calculator_rpn.compute(expression_4) == 4

    expression_5 = CalculatorExpression("10 5 2 - - 1 - 2 - 1 -")
    assert await calculator_rpn.compute(expression_5) == 3
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_multiply_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculatorExpression("3 4 *")
    assert await calculator_rpn.compute(expression_1) == 12

    expression_2 = CalculatorExpression("3 4 * 5 *")
    assert await calculator_rpn.compute(expression_2) == 60

    expression_3 = CalculatorExpression("3 4 * 5 * 2 *")
    assert await calculator_rpn.compute(expression_3) == 120

    expression_4 = CalculatorExpression("3 4 * 5 * 2 * 1 *")
    assert await calculator_rpn.compute(expression_4) == 120

    expression_5 = CalculatorExpression("3 4 * 5 * 2 * 1 * 2 *")
    assert await calculator_rpn.compute(expression_5) == 240
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_divide_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    expression_1 = CalculatorExpression("8 4 /")
    assert await calculator_rpn.compute(expression_1) == 2

    expression_2 = CalculatorExpression("8 4 2 / /")
    assert await calculator_rpn.compute(expression_2) == 4

    expression_3 = CalculatorExpression("8 4 2 / / 2 /")
    assert await calculator_rpn.compute(expression_3) == 2

    expression_4 = CalculatorExpression("8 4 2 / / 2 / 2 /")
    assert await calculator_rpn.compute(expression_4) == 1

    expression_5 = CalculatorExpression("8 4 2 / / 2 / 2 / 2 /")
    assert await calculator_rpn.compute(expression_5) == 0.5
    # fmt: on


# endregion-------------------------------------------------------------------------
