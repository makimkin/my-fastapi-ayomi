# endregion-------------------------------------------------------------------------
# region CALCULATOR HANDLERS
# ----------------------------------------------------------------------------------
from fastapi import status
from fastapi.routing import APIRouter

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from application.calculator.commands.compute import CalculatorComputeCommand
from infrastructure.dispatchers.dispatcher import Dispatcher

from .base import CALCULATOR_PREFIX, CALCULATOR_ACTIONS, CALCULATOR_TAG
from .schemas import CalculatorComputeRequest, CalculatorComputeResponse

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
        CalculatorComputeCommand(expression=request.expression)
    )


# endregion-------------------------------------------------------------------------
