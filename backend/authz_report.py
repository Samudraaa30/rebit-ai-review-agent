def generate_authz_findings(
    matches
):

    findings = []

    for match in matches:

        findings.append(
            {
                "severity": "MEDIUM",
                "status": "OPEN",
                "file": match["file"],
                "line": match["line"],
                "issue":
                    f"Authorization pattern detected ({match['type']})",
                "recommendation":
                    "Verify role-based access controls and permissions.",
                "code":
                    match["code"]
            }
        )

    return findings