import os
import time
from capture.screen_capture import capture_screen
from core.qa_engine import answer_from_screen

# Configuration
DELAY_TIME = 3 

def main():
    print("--- R2X Lite Screen Agent Interactive Mode ---")
    print(f"Instructions: Enter your question, then you will have {DELAY_TIME} seconds")
    print("to switch to the window you want to analyze.")
    print("Type 'exit' to stop.\n")

    while True:
        user_query = input("Ask a question: ").strip()

        if user_query.lower() in ['exit', 'quit']:
            break

        if not user_query:
            continue

        # Countdown delay
        print(f"Starting capture in...", end=" ", flush=True)
        for i in range(DELAY_TIME, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(1)
        print("BEEP!")

        try:
            # 1. Capture the screen after the delay
            img_object = capture_screen()

            # 2. Process with Vision AI
            print("Thinking...")
            answer = answer_from_screen(img_object, user_query)

            print(f"\n----- ANSWER -----\n{answer}\n")
            print("-" * 30)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()