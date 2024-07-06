import json

quiz_data = '''
[
    {
        "question": "What is the correct file extension for Python files?",
        "choices": [".py", ".python", ".pt", ".pyt"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "choices": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "How do you insert comments in Python code?",
        "choices": ["// This is a comment", "/* This is a comment */", "# This is a comment", "<!-- This is a comment -->"],
        "answer": "# This is a comment"
    },
    {
        "question": "What data type is the object below?\\nL = [1, 23, 'hello', 1]",
        "choices": ["Tuple", "Dictionary", "Array", "List"],
        "answer": "List"
    },
    {
        "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
        "choices": ["strip()", "ptrim()", "trim()", "len()"],
        "answer": "strip()"
    },
    {
        "question": "Which of the following statements is used to create an empty set?",
        "choices": ["{}", "[]", "()", "set()"],
        "answer": "set()"
    },
    {
        "question": "How do you start a while loop in Python?",
        "choices": ["while x > y:", "while (x > y)", "while x > y {", "while (x > y):"],
        "answer": "while x > y:"
    },
    {
        "question": "Which of the following functions checks if all items in an iterable are true?",
        "choices": ["all()", "any()", "check()", "every()"],
        "answer": "all()"
    },
    {
        "question": "Which of the following is not a valid data type in Python?",
        "choices": ["list", "tuple", "dict", "array"],
        "answer": "array"
    },
    {
        "question": "What is the output of the following code?\\nprint(type([]))",
        "choices": ["<class 'list'>", "<class 'tuple'>", "<class 'dictionary'>", "<class 'array'>"],
        "answer": "<class 'list'>"
    }
]
'''

questions = json.loads(quiz_data)

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Rules:")
    print("1. You will be presented with multiple-choice questions.")
    print("2. Type the number corresponding to your answer choice.")
    print("3. You will receive feedback on your answers.")
    print("4. Your score will be displayed at the end.\n")


# display the questions and take input from user
def present_question (question_data):
    print(question_data["question"])
    for idx, choice in enumerate(question_data["choices"], start=1):
        print(f"{idx}. {choice}")
    user_ans = input("Please Enter The Right Answer: ")
    return user_ans
    
# Checking if the answer is correct or not
def check_answer (user_ans, question_data):
    correct_ans = question_data["answer"]
    correct_choice = str(question_data["choices"].index(correct_ans) + 1)
    if user_ans == correct_choice:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer is: {correct_ans}\n")
        return False


def main ():
    play_again = True
    while play_again:
        display_welcome_message()
        score = 0
        for questin_data in questions:
            user_ans = present_question(questin_data)
            if check_answer(user_ans, questin_data):
                score += 1
        total_questions = len(questions)
        print(f"Your final score is {score}/{total_questions}.")
        performance = (score / total_questions) * 100
        print(f"Your performance: {performance:.2f}%\n")
        play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
        play_again = play_again_input == "yes"
    print("Thank you for playing the Quiz Game!")

if __name__ == "__main__":
    main()
