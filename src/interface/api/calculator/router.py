# endregion-------------------------------------------------------------------------
# region CALCULATOR HANDLERS
# ----------------------------------------------------------------------------------
import datetime
import io

from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter
from fastapi import Query, status

from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from application.calculation.commands import (
    CalculationComputeCommand,
    CalculationGenerateCSVCommand,
)
from application.calculation.queries import CalculationGetManyQuery

from infrastructure.dispatchers.dispatcher import Dispatcher

from .base import CALCULATOR_PREFIX, CALCULATOR_ACTIONS, CALCULATOR_TAG
from .schemas import (
    CalculatorComputeRequest,
    CalculatorComputeResponse,
    #
    CalculatorReadManyParams,
    CalculatorReadManyResponse,
)

router = APIRouter(
    prefix=CALCULATOR_PREFIX,
    route_class=DishkaRoute,
    tags=[CALCULATOR_TAG],
)


# endregion-------------------------------------------------------------------------
# region COMPUTE
# ----------------------------------------------------------------------------------
@router.post(
    CALCULATOR_ACTIONS.COMPUTE,
    status_code=status.HTTP_200_OK,
    response_model=CalculatorComputeResponse,
)
async def calculator_compute(
    request: CalculatorComputeRequest,
    dispatcher: FromDishka[Dispatcher],
):
    """-----------------------------------------------------------------------------
    Calculator compute endpoint.
    -----------------------------------------------------------------------------"""
    return await dispatcher.handle_command(
        CalculationComputeCommand(expression=request.expression)
    )


# endregion-------------------------------------------------------------------------
# region READ MANY
# ----------------------------------------------------------------------------------
@router.get(
    CALCULATOR_ACTIONS.READ_MANY,
    status_code=status.HTTP_200_OK,
    response_model=CalculatorReadManyResponse,
)
async def calculator_read_many(
    dispatcher: FromDishka[Dispatcher],
    params: Annotated[CalculatorReadManyParams, Query()],
):
    """-----------------------------------------------------------------------------
    Calculator read many endpoint.
    -----------------------------------------------------------------------------"""
    calculations = await dispatcher.handle_query(
        CalculationGetManyQuery(
            offset=params.offset,
            limit=params.limit,
        )
    )

    return {
        **params.model_dump(),
        "items": calculations,
    }


# endregion-------------------------------------------------------------------------
# region GENERATE CSV
# ----------------------------------------------------------------------------------
@router.get(
    CALCULATOR_ACTIONS.GENERATE_CSV,
    status_code=status.HTTP_200_OK,
)
async def calculator_generate_csv(dispatcher: FromDishka[Dispatcher]):
    """-----------------------------------------------------------------------------
    Calculator generate csv endpoint.
    -----------------------------------------------------------------------------"""
    csv_data = await dispatcher.handle_command(CalculationGenerateCSVCommand())

    csv_io = io.StringIO(csv_data)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return StreamingResponse(
        csv_io,
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=calculations_{now}.csv",
        },
    )


# endregion-------------------------------------------------------------------------
