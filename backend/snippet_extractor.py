from pathlib import Path


# Existing finding engine support
def extract_snippets(
    file_path,
    line_number
):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            lines = f.readlines()

        start = max(
            0,
            line_number - 3
        )

        end = min(
            len(lines),
            line_number + 2
        )

        return "".join(
            lines[start:end]
        )

    except Exception:

        return "Snippet unavailable"


# New Reasoning Agent support
def extract_relevant_snippets(
    relevant_files
):

    snippets = []

    for file_path in relevant_files:

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                lines = f.readlines()

            snippet = "".join(
                lines[:20]
            )

            snippets.append(
                {
                    "file": file_path,
                    "snippet": snippet
                }
            )

        except Exception:
            pass

    return snippets