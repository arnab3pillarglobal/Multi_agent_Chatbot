#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import MultiAgentChatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    print("Choose option:")
    print("1 - Ask a question for summary")
    print("2 - Generate MCQ questions")
    print("3 - Ask a question for answer")

    choice = input("Enter 1, 2 or 3: ").strip()

    user_input = input("Enter your input text or question: ")

    inputs = {}



    if choice == "1":
        inputs = {
            "input": user_input,
        }

    elif choice == "2":
        inputs = {
            "input": user_input,
        }
    elif choice == "3":
        inputs = {
            "input": user_input,
        }
    else:
        print("Invalid choice")
        return



    result = MultiAgentChatbot().crew().kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    run()