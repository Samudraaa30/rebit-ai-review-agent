from backend.tool_registry import (
    TOOLS
)

def run_tool(
    review_type,
    repo_path
):

    tool = TOOLS.get(
        review_type
    )

    if not tool:

        return []

    return tool.execute(
        repo_path
    )