def generate_html_report(
    filename,
    summary,
    findings,
    risk_score
):

    html = f"""
    <html>
    <head>
        <title>AI SSDLC Report</title>
    </head>
    <body>

    <h1>AI SSDLC Security Review Report</h1>

    <h2>Risk Score</h2>
    <p>{risk_score}/100</p>

    <h2>Executive Summary</h2>
    <p>{summary}</p>

    <h2>Top Findings</h2>
    """

    for finding in findings[:10]:

        html += f"""
        <hr>

        <h3>{finding.get('issue')}</h3>

        <p>
        Severity:
        {finding.get('severity')}
        </p>

        <p>
        File:
        {finding.get('file')}
        </p>

        <p>
        Recommendation:
        {finding.get('recommendation')}
        </p>
        """

    html += """
    </body>
    </html>
    """

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            html
        )

    return filename