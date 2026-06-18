from backend.tools.semgrep_tool import (
    run_semgrep
)

results = run_semgrep(
    "repos"
)

print(
    len(results)
)