import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

def review_chunk(
    chunk
):

    prompt = f"""
You are a cybersecurity reviewer.

Review this code chunk.

Identify:

1. Security Risks
2. Impact
3. Recommendation

Code:

{chunk}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Review Failed: {e}"