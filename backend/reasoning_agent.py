from pathlib import Path

def select_relevant_files(
    repo_path,
    review_type
):

    relevant_files = []

    keywords = []

    if review_type == "Input Validation":

        keywords = [
            "controller",
            "request",
            "input",
            "route",
            "api"
        ]

    elif review_type == "Authentication Review":

        keywords = [
            "auth",
            "login",
            "jwt",
            "security",
            "user"
        ]

    elif review_type == "Authorization Review":

        keywords = [
            "role",
            "permission",
            "access",
            "authorize"
        ]

    elif review_type == "Secrets Detection":

        keywords = [
            "secret",
            "token",
            "key",
            "password"
        ]

    for file in Path(repo_path).rglob("*"):

        if not file.is_file():
            continue

        file_name = str(
            file.name
        ).lower()

        for keyword in keywords:

            if keyword in file_name:

                relevant_files.append(
                    str(file)
                )

                break

    return relevant_files[:20]