# endregion-------------------------------------------------------------------------
# region BASE HANDLERS
# ----------------------------------------------------------------------------------
from fastapi.routing import APIRouter
from fastapi import status

from infrastructure.calculators.base import CalculatorBase

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .base import BASE_PREFIX, BASE_TAG, BASE_ACTIONS
from .schemas import BaseHealthCheckResponse

router = APIRouter(prefix=BASE_PREFIX, route_class=DishkaRoute, tags=[BASE_TAG])


@router.get(
    BASE_ACTIONS.HEALTHCHECK,
    status_code=status.HTTP_200_OK,
    response_model=BaseHealthCheckResponse,
)
async def base_health_check(
    calculator: FromDishka[CalculatorBase],
) -> dict:
    """-----------------------------------------------------------------------------
    The Base Health Check Handler.
    -----------------------------------------------------------------------------"""
    return {
        "calculator": {
            "name": calculator.__class__.__name__,
            "health": await calculator.check_health(),
        },
    }


# endregion-------------------------------------------------------------------------
