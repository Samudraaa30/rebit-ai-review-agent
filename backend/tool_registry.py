from backend.tools.input_validation_tool import (
    InputValidationTool
)

from backend.tools.secrets_tool import (
    SecretsTool
)

from backend.tools.auth_tool import (
    AuthTool
)

TOOLS = {

    "Input Validation":
        InputValidationTool(),

    "Secrets Detection":
        SecretsTool(),

    "Authentication Review":
        AuthTool()
}