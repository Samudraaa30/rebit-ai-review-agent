from pathlib import Path

WHITELIST_PATTERNS = [
    "matches(",
    "Pattern.compile(",
    "re.match(",
    "re.fullmatch(",
    "validator",
    "validate(",
    "sanitize(",
    "escape(",
    "express-validator",
    "joi",
    "yup",
    "zod",
    "@Valid",
    "@Validated"
]

def detect_whitelisting(repo_path):

    findings = []

    for file in Path(repo_path).rglob("*"):

        if file.suffix not in [
            ".java",
            ".py",
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

                for pattern in WHITELIST_PATTERNS:

                    if pattern.lower() in line.lower():

                        findings.append(
                            {
                                "file": str(file),
                                "line": line_num,
                                "type": "Whitelist / Validation Control",
                                "pattern": pattern,
                                "code": line.strip()
                            }
                        )

                        break

        except Exception:
            pass

    return findings