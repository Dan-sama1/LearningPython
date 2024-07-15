import random


def new_game():
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    guesses = []
    correct_guesses = 0
    question_num = 0
    for key in question_keys:
        print("-----------------")
        print(key)
        for i in choices[key]:
            print(i)
        while True:
            guess = input("Answer: ").upper()
            if guess in ['A', 'B', 'C', 'D']:
                guesses.append(guess)
                break
            else:
                print("Invalid Choices, Please Try Again...")
        correct_guesses += check_ans(questions[key], guess)
        question_num += 1
    display_score(correct_guesses, guesses, question_keys)


def check_ans(answer, guess):
    return 1 if answer == guess else 0


def display_score(correct, guesses, question_keys):
    input("Press ANY key to VIEW result...")
    print("--------------------------")
    print("\t\t  RESULTS")
    print("--------------------------")
    print("CORRECT ANSWERS: ", end="")
    for ans in question_keys:
        print(questions[ans], end=" ")
    print()
    print("\t\tGUESSES: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = correct
    print("--------------------------")
    print("YOUR SCORE IS:", score)
    print("--------------------------")


def play_again():
    while True:
        print("Play again? [Y/N]")
        again = input(">> ").upper()
        if again == 'Y':
            return True
        elif again == 'N':
            print("THANKS FOR PLAYING! :)")
            input("Press ANY key to continue...")
            break
        else:
            print("Invalid input, Please try again.")
            print('\n--------------------------')


questions = {
    "What is the correct way to declare a variable named age in Python and assign it the value 25? ": 'A',
    "Which of the following data types can store a collection of items in an ordered sequence? ": 'C',
    "What is the purpose of the def keyword in Python? ": 'A',
    "What does the concept of indentation signify in Python code? ": 'B',
    "What is the primary difference between a list and a tuple in Python? ": 'A'
}

choices = {
    "What is the correct way to declare a variable named age in Python and assign it the value 25? ":
        ["(a) age = 25", "(b) int age = 25", "(c) age(25)", "(d) age = 25"],
    "Which of the following data types can store a collection of items in an ordered sequence? ":
        ["(a) Integer", "(b) String", "(c) List", "(d) Boolean"],
    "What is the purpose of the def keyword in Python? ":
        ["(a) To define a function",
         "(b) To create a loop",
         "(c) To declare a variable",
         "(d) To import a library"],
    "What does the concept of indentation signify in Python code? ":
        ["(a) Whitespace is ignored",
         "(b) Indentation defines code blocks",
         "(c) Indentation is used for comments",
         "(d) Indentation is for visual formatting only"],
    "What is the primary difference between a list and a tuple in Python? ":
        ["(a) Lists are mutable, tuples are immutable",
         "(b) Tuples can hold different data types, lists cannot",
         "(c) Lists are faster for accessing elements, tuples are faster for modifications",
         "(d) Lists are used for numerical data, tuples are for strings"]
}

new_game()
while play_again():
    new_game()
