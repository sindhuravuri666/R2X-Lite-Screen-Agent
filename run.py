# run.py
from capture.screen_capture import capture_screen
from core.qa_engine import answer_from_screen

def main():
    print("Taking screenshot...")
    img = capture_screen()
    
    question = "what is the name of the current file?"
    print(f"Asking Gemini: {question}")
    
    answer = answer_from_screen(img, question)
    print(f"\n----- ANSWER -----\n{answer}")

if __name__ == "__main__":
    main()