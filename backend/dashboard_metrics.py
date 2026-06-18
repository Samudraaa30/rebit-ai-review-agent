def calculate_dashboard_metrics(
    history
):

    if not history:

        return None

    total_repositories = len(
        history
    )

    average_risk = round(

        sum(
            item["risk_score"]
            for item in history
        )

        / len(history),

        2
    )

    highest = max(
        history,
        key=lambda x:
        x["risk_score"]
    )

    latest = history[-1]

    return {

        "total_repositories":
            total_repositories,

        "average_risk":
            average_risk,

        "highest_repo":
            highest["repo"],

        "highest_score":
            highest["risk_score"],

        "latest_repo":
            latest["repo"]
    }