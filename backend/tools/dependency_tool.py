from backend.security_tool import (
    SecurityTool
)

from backend.dependency_detector import (
    detect_dependencies
)

class DependencyTool(
    SecurityTool
):

    name = "Dependency Security"

    def execute(
        self,
        repo_path
    ):

        return detect_dependencies(
            repo_path
        )