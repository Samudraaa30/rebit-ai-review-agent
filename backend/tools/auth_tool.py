from backend.security_tool import (
    SecurityTool
)

from backend.auth_detector import (
    detect_auth
)

from backend.auth_report import (
    generate_auth_findings
)

class AuthTool(
    SecurityTool
):

    name = "Authentication Review"

    def execute(
        self,
        repo_path
    ):

        matches = detect_auth(
            repo_path
        )

        return generate_auth_findings(
            matches
        )