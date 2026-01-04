import os
from openai import OpenAI


client = OpenAI()


def answer_from_screen(context: dict, question: str) -> str:
    """
    Answers a question using ONLY the extracted screen content.
    """

    content = context.get("content", "")

    prompt = f"""
You are a screen-aware assistant.

You must answer ONLY using the text content extracted from the user's screen.
If the answer is not present, say:

"I cannot find that information on this screen."

Screen Content:
----------------
{content}

User Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
