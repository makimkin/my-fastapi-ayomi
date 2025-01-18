# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR TESTS
# ----------------------------------------------------------------------------------
import pytest

from infrastructure.calculators.rpn import CalculatorRPN


@pytest.mark.asyncio
async def test_calculator_rpn_plus_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    assert await calculator_rpn.compute("3 4 +") == 7
    assert await calculator_rpn.compute("3 4 5 + +") == 12
    assert await calculator_rpn.compute("3 4 5 + + 2 +") == 14
    assert await calculator_rpn.compute("3 4 5 + + 2 + 1 +") == 15
    assert await calculator_rpn.compute("3 4 5 + + 2 + 1 + 2 +") == 17
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_substract_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    assert await calculator_rpn.compute("10 5 -") == 5
    assert await calculator_rpn.compute("10 5 2 - -") == 7
    assert await calculator_rpn.compute("10 5 2 - - 1 -") == 6
    assert await calculator_rpn.compute("10 5 2 - - 1 - 2 -") == 4
    assert await calculator_rpn.compute("10 5 2 - - 1 - 2 - 2 -") == 2
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_multiply_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    assert await calculator_rpn.compute("6 3 *") == 18
    assert await calculator_rpn.compute("6 3 2 * *") == 36
    assert await calculator_rpn.compute("6 3 2 * * 2 *") == 72
    assert await calculator_rpn.compute("6 3 2 * * 2 * 2 *") == 144
    assert await calculator_rpn.compute("6 3 2 * * 2 * 2 * 2 *") == 288
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_rpn_divide_operation() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    assert await calculator_rpn.compute("8 4 /") == 2
    assert await calculator_rpn.compute("8 4 2 / /") == 4
    assert await calculator_rpn.compute("8 4 2 / / 2 /") == 2
    assert await calculator_rpn.compute("8 4 2 / / 2 / 2 /") == 1
    assert await calculator_rpn.compute("8 4 2 / / 2 / 2 / 2 /") == 0.5
    # fmt: on


# endregion-------------------------------------------------------------------------
