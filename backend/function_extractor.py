import re

def extract_functions(file_path):

    functions = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            content = f.read()

        patterns = [
            r"def\s+(\w+)\(",
            r"function\s+(\w+)\(",
            r"public\s+.*?\s+(\w+)\("
        ]

        for pattern in patterns:

            matches = re.findall(
                pattern,
                content
            )

            functions.extend(
                matches
            )

    except Exception:
        pass

    return functions