from backend.security_tool import (
    SecurityTool
)

from backend.secret_detector import (
    detect_secrets
)

class SecretsTool(
    SecurityTool
):

    name = "Secrets Detection"

    def execute(
        self,
        repo_path
    ):

        return detect_secrets(
            repo_path
        )