# endregion-------------------------------------------------------------------------
# region APPLICATION FIELDS
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import AfterValidator, Field

from domain.calculator.value_objects import CalculatorExpression, CalculatorResult

from .validators import validate_str_value_object, validate_decimal_value_object


# endregion-------------------------------------------------------------------------
# region FIELDS
# ----------------------------------------------------------------------------------
FIELD_CALCULATOR_RESULT = Annotated[
    CalculatorResult | float,
    Field(description="The Calculator Result field"),
    AfterValidator(validate_decimal_value_object),
]

FIELD_CALCULATOR_EXPRESSION = Annotated[
    CalculatorExpression | str,
    Field(description="The Calculator Expression field"),
    AfterValidator(validate_str_value_object),
]

# endregion-------------------------------------------------------------------------
