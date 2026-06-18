import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

def select_relevant_files_ai(
    files,
    review_type
):

    file_list = "\n".join(
        files[:200]
    )

    prompt = f"""
You are a cybersecurity review agent.

Review Type:
{review_type}

Repository Files:
{file_list}

Select the 10 most relevant files.

Return only filenames.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Reasoning Failed: {e}"