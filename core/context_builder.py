from typing import Dict


def build_screen_context(ocr_text: str) -> Dict:
    """
    Builds a structured screen context object from OCR text.
    """

    if not ocr_text or ocr_text.strip() == "":
        content = "[No readable text detected on screen]"
    else:
        content = ocr_text.strip()

    context = {
        "source": "screen_capture",
        "content": content,
        "stats": {
            "char_count": len(content),
            "word_count": len(content.split()),
        }
    }

    return context


if __name__ == "__main__":
    print("This module is used inside the pipeline, not run directly.")
