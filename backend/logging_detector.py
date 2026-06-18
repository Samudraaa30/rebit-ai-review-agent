from pathlib import Path

LOG_PATTERNS = [
    "logger",
    "logging",
    "log",
    "audit",
    "exception",
    "trace",
    "monitor"
]

def detect_logging(
    repo_path
):

    findings = []

    for file in Path(repo_path).rglob("*"):

        if file.suffix not in [
            ".py",
            ".java",
            ".js",
            ".ts"
        ]:
            continue

        try:

            lines = file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).splitlines()

            for line_num, line in enumerate(
                lines,
                start=1
            ):

                for pattern in LOG_PATTERNS:

                    if pattern.lower() in line.lower():

                        findings.append(
                            {
                                "file": str(file),
                                "line": line_num,
                                "pattern": pattern,
                                "code": line.strip()
                            }
                        )

        except Exception:
            pass

    return findings