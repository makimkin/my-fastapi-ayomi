# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from interface.api.fields import (
    FIELD_CALCULATION_EXPRESSION,
    FIELD_CALCULATION_RESULT,
)


from ..schemas import APISchema

from pydantic import Field


# endregion-------------------------------------------------------------------------
# region COMPUTE
# ----------------------------------------------------------------------------------
class CalculatorComputeRequest(APISchema):
    expression: Annotated[str, Field(alias="expression")]


class CalculatorComputeResponse(APISchema):
    expression: Annotated[
        FIELD_CALCULATION_EXPRESSION,
        Field(alias="expression"),
    ]
    result: Annotated[
        FIELD_CALCULATION_RESULT,
        Field(alias="result"),
    ]


# endregion-------------------------------------------------------------------------
