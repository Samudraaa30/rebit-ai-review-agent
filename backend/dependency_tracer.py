import re

def trace_dependencies(
    file_path
):

    dependencies = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            content = f.read()

        calls = re.findall(
            r"(\w+)\(",
            content
        )

        dependencies.extend(
            list(set(calls))
        )

    except Exception:
        pass

    return dependencies[:30]