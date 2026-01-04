import keyboard
import time
import os
from capture.screen_capture import capture_screen
from core.qa_engine import answer_from_screen

# Configuration
HOTKEY = 'ctrl+shift+space' 

def trigger_assistant():
    print(f"\n[!] Hotkey detected! Starting analysis...")
    
    # Optional: Give yourself a tiny moment to let go of the keys
    time.sleep(0.5) 
    
    try:
        # 1. Capture the screen immediately
        img_object = capture_screen()
        
        # 2. For now, we will use a fixed question or prompt the terminal
        # (Later, this will be replaced by your Voice input)
        question = "Summarize what is on this screen and identify the active application."
        
        print("Thinking...")
        answer = answer_from_screen(img_object, question)
        
        print(f"\n----- SCREEN ANALYSIS -----\n{answer}\n")
        print(f"Waiting for {HOTKEY}...")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print(f"Assistant is ACTIVE. Press {HOTKEY} to analyze your screen.")
    print("Press 'esc' to close the assistant.")

    # Add the hotkey listener
    keyboard.add_hotkey(HOTKEY, trigger_assistant)

    # Keep the script running until 'esc' is pressed
    keyboard.wait('esc')

if __name__ == "__main__":
    main()