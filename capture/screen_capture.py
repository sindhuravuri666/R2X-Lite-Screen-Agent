from PIL import ImageGrab
from datetime import datetime
import os


def capture_screen(save_dir="data/screenshots"):
    """
    Captures the current screen and saves it as an image.
    Returns the saved image file path.
    """

    os.makedirs(save_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(save_dir, f"screen_{timestamp}.png")

    screenshot = ImageGrab.grab()
    screenshot.save(file_path)

    return file_path


if __name__ == "__main__":
    path = capture_screen()
    print(f"Screen captured → {path}")
