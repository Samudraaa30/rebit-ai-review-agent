from pathlib import Path

AUTHZ_PATTERNS = [
    "@PreAuthorize",
    "@RolesAllowed",
    "@Secured",
    "hasRole(",
    "hasAuthority(",
    "ROLE_ADMIN",
    "ROLE_USER",
    "permission",
    "permissions",
    "authorize",
    "accessControl",
    "access_control"
]

def detect_authorization(
    repo_path
):

    findings = []

    for file in Path(repo_path).rglob("*"):

        if file.suffix not in [
            ".java",
            ".js",
            ".ts",
            ".py"
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

                for pattern in AUTHZ_PATTERNS:

                    if pattern in line:

                        findings.append(
                            {
                                "file": str(file),
                                "line": line_num,
                                "type": pattern,
                                "code": line.strip()
                            }
                        )

        except Exception:
            pass

    return findings