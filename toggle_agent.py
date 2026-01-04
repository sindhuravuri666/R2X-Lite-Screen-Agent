import keyboard
import time
import tkinter as tk
from tkinter import simpledialog
import pygetwindow as gw
from capture.screen_capture import capture_screen
from core.qa_engine import answer_from_screen

HOTKEY = 'ctrl+shift+space'

def get_user_input():
    """Creates a hidden root window and shows a popup input dialog."""
    root = tk.Tk()
    root.withdraw() # Hide the main empty Tkinter window
    root.attributes("-topmost", True) # Keep it on top of all windows
    
    # Ask for the user's question
    user_query = simpledialog.askstring("Assistant", "Ask a question about this screen:")
    
    root.destroy() # Close the window completely after input
    return user_query

def trigger_assistant():
    print(f"\n[!] Hotkey detected!")
    
    # Optional: Small delay to ensure the screen is stable
    time.sleep(0.5) 
    
    try:
        # 1. Get user query via GUI popup
        question = get_user_input()
        
        # If the user cancels or types nothing, stop
        if not question:
            return

        # 2. Grab context (window title)
        active_window = gw.getActiveWindow()
        window_title = active_window.title if active_window else "Unknown"

        # 3. Capture and analyze
        print("Analyzing...")
        img_object = capture_screen()
        full_prompt = f"Active Window: {window_title}. {question}"
        
        answer = answer_from_screen(img_object, full_prompt)
        print(f"\n----- ANSWER -----\n{answer}\n")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print(f"Assistant active. Press {HOTKEY} to ask about your current screen.")
    keyboard.add_hotkey(HOTKEY, trigger_assistant)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()