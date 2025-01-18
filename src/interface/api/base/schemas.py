# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from ..schemas import APISchema

from pydantic import Field


# endregion-------------------------------------------------------------------------
# region HEALTHCHECK
# ----------------------------------------------------------------------------------
class BaseHealthCheckResponseStatus(APISchema):
    name: Annotated[str, Field(alias="name")]
    health: Annotated[bool, Field(alias="health")]


class BaseHealthCheckResponse(APISchema):
    calculator: Annotated[
        BaseHealthCheckResponseStatus,
        Field(alias="calculator"),
    ]
    calculations_csv_builder: Annotated[
        BaseHealthCheckResponseStatus,
        Field(alias="calculationsCSVBuilder"),
    ]
    calculation_repository: Annotated[
        BaseHealthCheckResponseStatus,
        Field(alias="calculationRepository"),
    ]


# endregion-------------------------------------------------------------------------
