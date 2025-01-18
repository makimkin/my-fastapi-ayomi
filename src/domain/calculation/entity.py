# endregion-------------------------------------------------------------------------
# region CALCULATION ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from decimal import Decimal

from domain.calculation.value_objects import (
    CalculationExpression,
    CalculationResult,
)
from domain.common.value_object import EntityCreatedAt, EntityId

from ..common.entity import EntityBase

KEY_ID = "id"
KEY_RESULT = "result"
KEY_CREATED_AT = "created_at"
KEY_EXPRESSION = "expression"


@dataclass(eq=False, kw_only=True)
class CalculationEntity(EntityBase):
    calculation_id: EntityId = field(
        default_factory=lambda: EntityId.create(),
        metadata={
            "optional": False,
            "description": "The unique identifier of the entity.",
        },
    )

    created_at: EntityCreatedAt = field(
        default_factory=lambda: EntityCreatedAt.create(),
        metadata={
            "optional": False,
            "description": "The date and time the entity was created.",
        },
    )

    expression: CalculationExpression = field(
        metadata={
            "optional": False,
            "description": "The expression to calculate.",
        }
    )
    result: CalculationResult | None = field(
        default=None,
        metadata={
            "optional": True,
            "description": "The result of the calculation.",
        },
    )

    def _to_dict(self) -> dict:
        return {
            **super()._to_dict(),
            KEY_ID: self.calculation_id.as_raw(),
            KEY_EXPRESSION: self.expression.as_raw(),
            KEY_CREATED_AT: self.created_at.as_raw(),
            KEY_RESULT: float(self.result.as_raw()) if self.result else None,
        }

    @classmethod
    def from_dict(cls, document: dict) -> "CalculationEntity":
        calculation_id = EntityId(document[KEY_ID])
        created_at = EntityCreatedAt(document[KEY_CREATED_AT])
        expression = CalculationExpression(document[KEY_EXPRESSION])
        result = (
            None
            if document[KEY_RESULT] is None
            else CalculationResult(Decimal.from_float(document[KEY_RESULT]))
        )

        return cls(
            result=result,
            created_at=created_at,
            expression=expression,
            calculation_id=calculation_id,
        )


# endregion-------------------------------------------------------------------------
