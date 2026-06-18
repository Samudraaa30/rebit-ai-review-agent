from backend.security_tool import (
    SecurityTool
)

from backend.authz_detector import (
    detect_authorization
)

from backend.authz_report import (
    generate_authz_findings
)

class AuthzTool(
    SecurityTool
):

    name = "Authorization Review"

    def execute(
        self,
        repo_path
    ):

        matches = detect_authorization(
            repo_path
        )

        return generate_authz_findings(
            matches
        )