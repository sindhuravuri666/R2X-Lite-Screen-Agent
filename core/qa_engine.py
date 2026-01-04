import os
from google import genai
from PIL import Image

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Your confirmed working model for 2026
MODEL_NAME = "gemini-2.5-flash-lite"

def answer_from_screen(img_input, question: str) -> str:
    """
    img_input can be:
    1. A string path (e.g., "data/screenshots/test.png")
    2. A PIL Image object (the direct output from capture_screen())
    """
    # If the input is a path, we open it. Otherwise, we assume it's the image.
    if isinstance(img_input, str):
        img = Image.open(img_input)
    else:
        img = img_input

    prompt = f"You are a screen agent. {question}"

    try:
        # The SDK automatically handles PIL Image objects
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt, img]
        )
        return response.text.strip()
    except Exception as e:
        return f"[Error] {e}"