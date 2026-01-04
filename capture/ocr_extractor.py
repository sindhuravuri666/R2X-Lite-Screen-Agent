import pytesseract
from PIL import Image
import os

# 1. POINT TO THE TESSERACT EXECUTABLE
# Change this path if you installed Tesseract in a different location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    Returns cleaned text output.
    """
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Perform OCR
        raw_text = pytesseract.image_to_string(image)
        
        return raw_text.strip()
    
    except Exception as e:
        return f"Error during OCR: {e}"

if __name__ == "__main__":
    # 2. TEST CASE FIX
    # Make sure 'test_image' points to an actual file, not a folder
    test_image = "data/screenshots/test_capture.png" 
    
    if os.path.exists(test_image):
        print(f"Extracted Text: {extract_text_from_image(test_image)}")
    else:
        print(f"File not found: {test_image}. This file is meant to be used from pipeline.")