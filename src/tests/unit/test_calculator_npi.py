# endregion-------------------------------------------------------------------------
# region REVERSE POLISH NOTATION CALCULATOR TESTS
# ----------------------------------------------------------------------------------
import pytest

from infrastructure.calculators.rpn import CalculatorRPN


@pytest.mark.asyncio
async def test_calculator_rpn_simple_operations() -> None:
    """-----------------------------------------------------------------------------
    Test simple operations.
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_rpn = CalculatorRPN()

    assert await calculator_rpn.compute("3 4 +") == 7
    assert await calculator_rpn.compute("10 5 -") == 5
    assert await calculator_rpn.compute("6 3 *") == 18
    assert await calculator_rpn.compute("8 4 /") == 2
    # fmt: on


# endregion-------------------------------------------------------------------------
