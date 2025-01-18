# endregion-------------------------------------------------------------------------
# region CALCULATION ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from decimal import Decimal

from domain.calculator.value_objects import CalculatorExpression, CalculatorResult

from ..common.entity import EntityBase


KEY_EXPRESSION = "expression"
KEY_RESULT = "result"


@dataclass(eq=False, kw_only=True)
class CalculatorEntity(EntityBase):
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
            KEY_EXPRESSION: self.expression.as_raw(),
            KEY_RESULT: float(self.result.as_raw()) if self.result else None,
        }

    @classmethod
    def from_dict(cls, document: dict) -> "EntityBase":
        return cls(
            expression=CalculatorExpression(document[KEY_EXPRESSION]),
            result=CalculatorResult(Decimal.from_float(document[KEY_RESULT]))
            if document[KEY_RESULT]
            else None,
        )


# endregion-------------------------------------------------------------------------
