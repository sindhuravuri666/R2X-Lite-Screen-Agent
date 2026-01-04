import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Use the exact string from your successful list
MODEL_NAME = "gemini-2.5-flash-lite"

def answer_from_screen(context: dict, question: str) -> str:
    screen_text = context.get("content", "")

    prompt = f"""
You are a screen-aware assistant.
Only use the information found in the extracted on-screen text.
Do NOT guess or use outside knowledge.

Screen Content:
----------------
{screen_text}

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"[Gemini Error] {e}"