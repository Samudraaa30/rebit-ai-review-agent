import subprocess
import json

def run_gitleaks(
    repo_path
):

    try:

        result = subprocess.run(
            [
                "gitleaks",
                "detect",
                repo_path,
                "--report-format",
                "json"
            ],
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return []

        return json.loads(
            result.stdout
        )

    except Exception as e:

        return [
            {
                "error":
                    str(e)
            }
        ]