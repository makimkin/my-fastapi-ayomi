# endregion-------------------------------------------------------------------------
# region CALCULATION ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from decimal import Decimal

from domain.calculator.value_objects import CalculatorExpression, CalculatorResult
from domain.common.value_object import EntityCreatedAt, EntityId

from ..common.entity import EntityBase

KEY_ID = "id"
KEY_CREATED_AT = "created_at"
KEY_EXPRESSION = "expression"
KEY_RESULT = "result"


@dataclass(eq=False, kw_only=True)
class CalculatorEntity(EntityBase):
    id: EntityId = field(
        default_factory=lambda: EntityId.create(),
        metadata={
            "optional": True,
            "description": "The unique identifier of the entity.",
        },
    )

    created_at: EntityCreatedAt = field(
        default_factory=lambda: EntityCreatedAt.create(),
        metadata={
            "optional": True,
            "description": "The date and time the entity was created.",
        },
    )

    expression: CalculatorExpression = field(
        metadata={
            "optional": False,
            "description": "The expression to calculate.",
        }
    )
    result: CalculatorResult | None = field(
        default=None,
        metadata={
            "optional": True,
            "description": "The result of the calculation.",
        },
    )

    def _to_dict(self) -> dict:
        return {
            **super()._to_dict(),
            KEY_ID: self.id.as_raw(),
            KEY_EXPRESSION: self.expression.as_raw(),
            KEY_CREATED_AT: self.created_at.as_raw(),
            KEY_RESULT: float(self.result.as_raw()) if self.result else None,
        }

    @classmethod
    def from_dict(cls, document: dict) -> "CalculatorEntity":
        id = EntityId(document[KEY_ID])
        created_at = EntityCreatedAt(document[KEY_CREATED_AT])
        expression = CalculatorExpression(document[KEY_EXPRESSION])
        result = (
            None
            if document[KEY_RESULT] is None
            else CalculatorResult(Decimal.from_float(document[KEY_RESULT]))
        )

        return cls(
            id=id,
            result=result,
            created_at=created_at,
            expression=expression,
        )


# endregion-------------------------------------------------------------------------
