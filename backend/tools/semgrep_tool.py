import subprocess
import json

def run_semgrep(
    repo_path
):

    try:

        result = subprocess.run(
            [
                "semgrep",
                "--config",
                "auto",
                repo_path,
                "--json"
            ],
            capture_output=True,
            text=True
        )

        data = json.loads(
            result.stdout
        )

        return data.get(
            "results",
            []
        )

    except Exception as e:

        return [
            {
                "error":
                    str(e)
            }
        ]