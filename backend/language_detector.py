from pathlib import Path

def detect_language(repo_path):

    counts = {
        "Python": 0,
        "Java": 0,
        "JavaScript": 0,
        "TypeScript": 0
    }

    for file in Path(repo_path).rglob("*"):

        suffix = file.suffix.lower()

        if suffix == ".py":
            counts["Python"] += 1

        elif suffix == ".java":
            counts["Java"] += 1

        elif suffix == ".js":
            counts["JavaScript"] += 1

        elif suffix == ".ts":
            counts["TypeScript"] += 1

    language = max(
        counts,
        key=counts.get
    )

    return {
        "language": language,
        "counts": counts
    }