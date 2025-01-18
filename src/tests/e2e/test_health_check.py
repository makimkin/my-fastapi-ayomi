# endregion-------------------------------------------------------------------------
# region HEALTH CHECK TESTS
# ----------------------------------------------------------------------------------
import pytest

from fastapi import status

from interface.api.base.base import BASE_ACTIONS, BASE_PREFIX
from interface.api.base.schemas import (
    BaseHealthCheckResponse,
)

from .conftest import ContextTest


@pytest.mark.asyncio
async def test_health_check_success(context: ContextTest) -> None:
    """-----------------------------------------------------------------------------
    Test health check success.
    -----------------------------------------------------------------------------"""
    # fmt: off
    health_check_response = await context.get(f"/v1{BASE_PREFIX}{BASE_ACTIONS.HEALTHCHECK}")
    assert health_check_response.status_code == status.HTTP_200_OK, health_check_response.text

    health_check_json, text = health_check_response.json(), health_check_response.text
    assert "calculator" in health_check_json, text
    assert "health" in health_check_json["calculator"], text
    assert "name" in health_check_json["calculator"], text

    assert "calculationsCSVBuilder" in health_check_json, text
    assert "health" in health_check_json["calculationsCSVBuilder"], text
    assert "name" in health_check_json["calculationsCSVBuilder"], text

    assert "calculationRepository" in health_check_json, text
    assert "health" in health_check_json["calculationRepository"], text
    assert "name" in health_check_json["calculationRepository"], text

    health_check_data = BaseHealthCheckResponse(**health_check_json)
    assert health_check_data.calculator is not None, text
    assert health_check_data.calculator.health == "✅", text
    assert health_check_data.calculator.name is not None, text

    assert health_check_data.calculation_repository is not None, text
    assert health_check_data.calculation_repository.health == "✅", text
    assert health_check_data.calculation_repository.name is not None, text

    assert health_check_data.calculations_csv_builder is not None, text
    assert health_check_data.calculations_csv_builder.health == "✅", text
    assert health_check_data.calculations_csv_builder.name is not None, text
    # fmt: on


# endregion-------------------------------------------------------------------------
