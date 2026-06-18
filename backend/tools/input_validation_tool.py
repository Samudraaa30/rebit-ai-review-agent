from backend.security_tool import (
    SecurityTool
)

from backend.source_detector import (
    detect_sources
)

from backend.validation_detector import (
    detect_validations
)

from backend.sink_detector import (
    detect_sinks
)

from backend.finding_engine import (
    generate_findings
)

class InputValidationTool(
    SecurityTool
):

    name = "Input Validation"

    def execute(
        self,
        repo_path
    ):

        sources = detect_sources(
            repo_path
        )

        validations = detect_validations(
            repo_path
        )

        sinks = detect_sinks(
            repo_path
        )

        return generate_findings(
            sources,
            validations,
            sinks
        )