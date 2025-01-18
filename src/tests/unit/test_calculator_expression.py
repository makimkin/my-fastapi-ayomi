# endregion-------------------------------------------------------------------------
# region CALCULATOR EXPRESSION TESTS
# ----------------------------------------------------------------------------------
import pytest

from domain.calculator.exceptions import (
    CalculatorExpressionInvalidCharacterException,
)
from domain.calculator.value_objects import CalculatorExpression

from domain.calculator.value_objects.expression import CalculatorOperands


@pytest.mark.asyncio
async def test_calculator_expression_to_list() -> None:
    """-----------------------------------------------------------------------------
    Test calculator expression to list method.
    -----------------------------------------------------------------------------"""
    # fmt: off
    # test 1️⃣
    calculator_expression_1 = CalculatorExpression("3 4 +")

    calculator_expression_list_1 = calculator_expression_1.to_list()

    assert len(calculator_expression_list_1) == 3
    assert calculator_expression_list_1[0] == 3
    assert calculator_expression_list_1[1] == 4
    assert calculator_expression_list_1[2] == CalculatorOperands.ADD

    # test 2️⃣
    calculator_expression_2 = CalculatorExpression("3 4 * 5 +")

    calculator_expression_list_2 = calculator_expression_2.to_list()

    assert len(calculator_expression_list_2) == 5
    assert calculator_expression_list_2[0] == 3
    assert calculator_expression_list_2[1] == 4
    assert calculator_expression_list_2[2] == CalculatorOperands.MULTIPLY
    assert calculator_expression_list_2[3] == 5
    assert calculator_expression_list_2[4] == CalculatorOperands.ADD

    # test 3️⃣
    calculator_expression_3 = CalculatorExpression("3 4 * 5 / 2 -")

    calculator_expression_list_3 = calculator_expression_3.to_list()

    assert len(calculator_expression_list_3) == 7
    assert calculator_expression_list_3[0] == 3
    assert calculator_expression_list_3[1] == 4
    assert calculator_expression_list_3[2] == CalculatorOperands.MULTIPLY
    assert calculator_expression_list_3[3] == 5
    assert calculator_expression_list_3[4] == CalculatorOperands.DIVIDE
    assert calculator_expression_list_3[5] == 2
    assert calculator_expression_list_3[6] == CalculatorOperands.SUBTRACT

    # test 4️⃣
    calculator_expression_4 = CalculatorExpression("3 4 * 5 / 2 - 1 +")

    calculator_expression_list_4 = calculator_expression_4.to_list()

    assert len(calculator_expression_list_4) == 9
    assert calculator_expression_list_4[0] == 3
    assert calculator_expression_list_4[1] == 4
    assert calculator_expression_list_4[2] == CalculatorOperands.MULTIPLY
    assert calculator_expression_list_4[3] == 5
    assert calculator_expression_list_4[4] == CalculatorOperands.DIVIDE
    assert calculator_expression_list_4[5] == 2
    assert calculator_expression_list_4[6] == CalculatorOperands.SUBTRACT
    assert calculator_expression_list_4[7] == 1
    assert calculator_expression_list_4[8] == CalculatorOperands.ADD
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_expression_strip() -> None:
    """-----------------------------------------------------------------------------
    -----------------------------------------------------------------------------"""
    # fmt: off
    calculator_expression_1 = CalculatorExpression(" 3 4 + ")
    assert calculator_expression_1.as_raw() == "3 4 +"

    calculator_expression_2 = CalculatorExpression(" 3 4 +")
    assert calculator_expression_2.as_raw() == "3 4 +"

    calculator_expression_3 = CalculatorExpression("3 4 + ")
    assert calculator_expression_3.as_raw() == "3 4 +"

    calculator_expression_4 = CalculatorExpression("3 4 +")
    assert calculator_expression_4.as_raw() == "3 4 +"

    calculator_expression_5 = CalculatorExpression(" 3 4 +  ")
    assert calculator_expression_5.as_raw() == "3 4 +"
    # fmt: on


@pytest.mark.asyncio
async def test_calculator_expression_error_invalid() -> None:
    """-----------------------------------------------------------------------------
    -----------------------------------------------------------------------------"""
    # fmt: off
    with pytest.raises(CalculatorExpressionInvalidCharacterException):
        CalculatorExpression("3 4 a 5")


    with pytest.raises(CalculatorExpressionInvalidCharacterException):
        CalculatorExpression("3 4 5 b")

    with pytest.raises(CalculatorExpressionInvalidCharacterException):
        CalculatorExpression("3 4 c 5 c")

    with pytest.raises(CalculatorExpressionInvalidCharacterException):
        CalculatorExpression("3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z")

    with pytest.raises(CalculatorExpressionInvalidCharacterException):
        CalculatorExpression("3 4 5 6 + + d")
    # fmt: on


# endregion-------------------------------------------------------------------------
