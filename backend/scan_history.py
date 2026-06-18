import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = "scan_history.json"

def save_scan(
    repo_url,
    review_type,
    risk_score
):

    history = []

    if Path(HISTORY_FILE).exists():

        with open(
            HISTORY_FILE,
            "r"
        ) as f:

            history = json.load(f)

    history.append(
        {
            "repo": repo_url,
            "review_type": review_type,
            "risk_score": risk_score,
            "timestamp": str(
                datetime.now()
            )
        }
    )

    with open(
        HISTORY_FILE,
        "w"
    ) as f:

        json.dump(
            history,
            f,
            indent=4
        )

def load_history():

    if not Path(
        HISTORY_FILE
    ).exists():

        return []

    with open(
        HISTORY_FILE,
        "r"
    ) as f:

        return json.load(f)