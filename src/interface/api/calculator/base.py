# endregion-------------------------------------------------------------------------
# region CALCULATOR API
# ----------------------------------------------------------------------------------
from ..actions import Actions

CALCULATOR_PREFIX = "/calculator"
CALCULATOR_TAG = "Calculator"


class CALCULATOR_ACTIONS(Actions):
    COMPUTE = "/compute"

    READ_MANY = "/"

    GENERATE_CSV = "/csv"


# endregion-------------------------------------------------------------------------
