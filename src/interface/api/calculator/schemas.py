# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from interface.api.fields import (
    FIELD_CALCULATION_EXPRESSION,
    FIELD_CALCULATION_RESULT,
    FIELD_ENTITY_CREATED_AT,
    FIELD_ENTITY_ID,
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
# region READ MANY
# ----------------------------------------------------------------------------------
class CalculatorReadManyParams(APISchema):
    pass


class CalculatorReadManyResponseItem(APISchema):
    calculation_id: Annotated[
        FIELD_ENTITY_ID,
        Field(alias="id"),
    ]
    created_at: Annotated[
        FIELD_ENTITY_CREATED_AT,
        Field(alias="createdAt"),
    ]
    expression: Annotated[
        FIELD_CALCULATION_EXPRESSION,
        Field(alias="expression"),
    ]
    result: Annotated[
        FIELD_CALCULATION_RESULT,
        Field(alias="result"),
    ]


class CalculatorReadManyResponse(CalculatorReadManyParams):
    items: list[CalculatorReadManyResponseItem]


# endregion-------------------------------------------------------------------------
