import datetime
import os
from PIL import ImageGrab
import win32gui


def get_active_window_bbox():
    hwnd = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(hwnd)
    return rect  # (left, top, right, bottom)


def capture_screen() -> str:
    os.makedirs("data/screenshots", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/screenshots/active_window_{timestamp}.png"

    left, top, right, bottom = get_active_window_bbox()

    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img.save(filename)

    print(f"Active window captured → {filename}")
    return filename
