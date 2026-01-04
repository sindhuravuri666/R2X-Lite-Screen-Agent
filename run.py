import os
import sys
from capture.screen_capture import capture_screen
from core.qa_engine import answer_from_screen

def main():
    print("--- R2X Lite Screen Agent Interactive Mode ---")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        # 1. Ask the user for a question first
        user_query = input("Ask a question about your screen: ").strip()

        if user_query.lower() in ['exit', 'quit']:
            print("Shutting down...")
            break

        if not user_query:
            continue

        try:
            # 2. Capture the screen only when a question is asked
            print("Capturing screen...")
            img_object = capture_screen()

            # 3. Get the answer using the direct PIL object
            print("Thinking...")
            answer = answer_from_screen(img_object, user_query)

            print(f"\n----- ANSWER -----\n{answer}\n")
            print("-" * 30)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()