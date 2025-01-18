# endregion-------------------------------------------------------------------------
# region BASE HANDLERS
# ----------------------------------------------------------------------------------
from fastapi.routing import APIRouter
from fastapi import status

from infrastructure.csv_builder.calculations.base import CalculationsCSVBuilderBase
from infrastructure.calculators.base import CalculatorBase

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from infrastructure.repositories.calculation.base import CalculationRepositoryBase

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
    calculations_repository: FromDishka[CalculationRepositoryBase],
    calculations_csv_builder: FromDishka[CalculationsCSVBuilderBase],
) -> dict:
    """-----------------------------------------------------------------------------
    The Base Health Check Handler.
    -----------------------------------------------------------------------------"""
    return {
        "calculator": {
            "name": calculator.__class__.__name__,
            "health": await calculator.check_health(),
        },
        "calculations_csv_builder": {
            "name": calculations_csv_builder.__class__.__name__,
            "health": True,
        },
        "calculation_repository": {
            "name": calculations_repository.__class__.__name__,
            "health": True,
        },
    }


# endregion-------------------------------------------------------------------------
