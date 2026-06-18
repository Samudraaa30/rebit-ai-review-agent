from backend.security_tool import (
    SecurityTool
)

from backend.logging_detector import (
    detect_logging
)

class LoggingTool(
    SecurityTool
):

    name = "Logging & Monitoring"

    def execute(
        self,
        repo_path
        ):

        return detect_logging(
            repo_path
        )