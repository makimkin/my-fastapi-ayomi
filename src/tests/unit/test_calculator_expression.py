# endregion-------------------------------------------------------------------------
# region CALCULATION EXPRESSION TESTS
# ----------------------------------------------------------------------------------
import pytest

from domain.calculation.exceptions import (
    CalculationExpressionInvalidCharacterException,
)
from domain.calculation.value_objects import CalculationExpression

from domain.calculation.value_objects.expression import CalculationOperands


@pytest.mark.asyncio
async def test_calculation_expression_to_list() -> None:
    """-----------------------------------------------------------------------------
    Test calculation expression to list method.
    -----------------------------------------------------------------------------"""
    # fmt: off
    # test 1️⃣
    calculation_expression_1 = CalculationExpression("3 4 +")

    calculation_expression_list_1 = calculation_expression_1.to_list()

    assert len(calculation_expression_list_1) == 3
    assert calculation_expression_list_1[0] == 3
    assert calculation_expression_list_1[1] == 4
    assert calculation_expression_list_1[2] == CalculationOperands.ADD

    # test 2️⃣
    calculation_expression_2 = CalculationExpression("3 4 * 5 +")

    calculation_expression_list_2 = calculation_expression_2.to_list()

    assert len(calculation_expression_list_2) == 5
    assert calculation_expression_list_2[0] == 3
    assert calculation_expression_list_2[1] == 4
    assert calculation_expression_list_2[2] == CalculationOperands.MULTIPLY
    assert calculation_expression_list_2[3] == 5
    assert calculation_expression_list_2[4] == CalculationOperands.ADD

    # test 3️⃣
    calculation_expression_3 = CalculationExpression("3 4 * 5 / 2 -")

    calculation_expression_list_3 = calculation_expression_3.to_list()

    assert len(calculation_expression_list_3) == 7
    assert calculation_expression_list_3[0] == 3
    assert calculation_expression_list_3[1] == 4
    assert calculation_expression_list_3[2] == CalculationOperands.MULTIPLY
    assert calculation_expression_list_3[3] == 5
    assert calculation_expression_list_3[4] == CalculationOperands.DIVIDE
    assert calculation_expression_list_3[5] == 2
    assert calculation_expression_list_3[6] == CalculationOperands.SUBTRACT

    # test 4️⃣
    calculation_expression_4 = CalculationExpression("3 4 * 5 / 2 - 1 +")

    calculation_expression_list_4 = calculation_expression_4.to_list()

    assert len(calculation_expression_list_4) == 9
    assert calculation_expression_list_4[0] == 3
    assert calculation_expression_list_4[1] == 4
    assert calculation_expression_list_4[2] == CalculationOperands.MULTIPLY
    assert calculation_expression_list_4[3] == 5
    assert calculation_expression_list_4[4] == CalculationOperands.DIVIDE
    assert calculation_expression_list_4[5] == 2
    assert calculation_expression_list_4[6] == CalculationOperands.SUBTRACT
    assert calculation_expression_list_4[7] == 1
    assert calculation_expression_list_4[8] == CalculationOperands.ADD
    # fmt: on


@pytest.mark.asyncio
async def test_calculation_expression_strip() -> None:
    """-----------------------------------------------------------------------------
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculation_expression_1 = CalculationExpression(" 3 4 + ")
    assert calculation_expression_1.as_raw() == "3 4 +"

    calculation_expression_2 = CalculationExpression(" 3 4 +")
    assert calculation_expression_2.as_raw() == "3 4 +"

    calculation_expression_3 = CalculationExpression("3 4 + ")
    assert calculation_expression_3.as_raw() == "3 4 +"

    calculation_expression_4 = CalculationExpression("3 4 +")
    assert calculation_expression_4.as_raw() == "3 4 +"

    calculation_expression_5 = CalculationExpression(" 3 4 +  ")
    assert calculation_expression_5.as_raw() == "3 4 +"
    # fmt: on


@pytest.mark.asyncio
async def test_calculation_expression_error_invalid() -> None:
    """-----------------------------------------------------------------------------
    -----------------------------------------------------------------------------"""
    # fmt: off
    with pytest.raises(CalculationExpressionInvalidCharacterException):
        CalculationExpression("3 4 a 5")


    with pytest.raises(CalculationExpressionInvalidCharacterException):
        CalculationExpression("3 4 5 b")

    with pytest.raises(CalculationExpressionInvalidCharacterException):
        CalculationExpression("3 4 c 5 c")

    with pytest.raises(CalculationExpressionInvalidCharacterException):
        CalculationExpression("3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z")

    with pytest.raises(CalculationExpressionInvalidCharacterException):
        CalculationExpression("3 4 5 6 + + d")
    # fmt: on


# endregion-------------------------------------------------------------------------
