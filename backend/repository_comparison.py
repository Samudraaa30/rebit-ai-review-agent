def compare_repositories(
    history
):

    if len(history) < 2:

        return None

    latest = history[-1]

    previous = history[-2]

    return {
        "latest_repo":
            latest["repo"],

        "latest_score":
            latest["risk_score"],

        "previous_repo":
            previous["repo"],

        "previous_score":
            previous["risk_score"],

        "difference":
            latest["risk_score"]
            -
            previous["risk_score"]
    }