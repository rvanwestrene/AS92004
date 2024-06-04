import random


# Simple checker for yes no input
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please enter yes or no")


# int checker, flexable min/max values,
def int_input(prompt, min_value=None, max_value=None):
    # determine the error message based on function call variables
    if min_value is not None and max_value is not None:  # min and max
        error = f"Please enter a number between {min_value} and {max_value}."
    elif min_value is not None and max_value is None:  # min only
        error = f"Please enter a number {min_value} or higher."
    elif min_value is None and max_value is not None:  # max only
        error = f"Please enter a number that is {max_value} or lower."
    else:
        error = f"Please enter a number."
    # loop until valid input detected
    while True:
        response = input(prompt).lower()
        try:
            response = int(response)
            if min_value is not None and response < min_value:
                print(error)
            elif max_value is not None and response > max_value:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# generates a question based off difficulty chosen
def question_maker(challenge_level):
    if challenge_level == 1:
        letter_list = ["A", "B", "C"]
        return "A, B, or C? ", letter_list, random.choice(letter_list)
    elif challenge_level == 2:
        letter_list = ["A", "B", "C", "D"]
        return "A, B, C, or D? ", letter_list, random.choice(letter_list)
    else:
        letter_list = ["A", "B", "C", "D", "E"]
        return "A, B, C, D, or E? ", letter_list, random.choice(letter_list)
# returns the question, the list of possible answers, and the answer chosen from that list of answers


# checks user input against correct answer, making sure it is within the range of possible answers, if not: loop
def answer_input(correct_answer, possible_letters):
    while True:
        response = input().upper()
        if response == correct_answer:
            return True, response
        elif response in possible_letters:
            return False, response
        else:
            print("Please enter one of the letters... 🤡")


# simply prints instructions
def instructions():
    print("Step right up! Guess the random letter! Win a prize! 🤡")


total_correct = 0
quiz_history = []

# Main routine
print("✨✨✨ Mr V's Pretend Quiz! ✨✨✨")
print()
if yes_no("Do you want to read the instructions? "):
    instructions()

# quiz variable setup
difficulty = int_input("Choose a difficulty! (1,2, or 3): ", 1, 3)
questions = int_input("How many questions do you want to attempt? ", 1)
cheat_mode = yes_no("Do you want me to help you? (cheat mode) ")
print()

# store cheat status to history
quiz_history.append("Cheats were active!")
quiz_history.append("")

# Core quiz loop
for i in range(1, questions + 1):
    # generate question
    question_info = question_maker(difficulty)

    # set up question and store history
    title = f"Question {i}!"
    print(title)
    print(question_info[0])
    quiz_history.append(title)
    quiz_history.append(question_info[0])
    quiz_history.append(f"The answer was: {question_info[2]}")

    # only print this if in cheat mode
    if cheat_mode:
        print(f"Psst! Try {question_info[2]} 🤡")

    # get whether the user answered correctly and what they wrote
    guess = answer_input(question_info[2], question_info[1])
    if guess[0]:  # if correct
        total_correct += 1
        print("🎇 You got it! Well done! 🤡")
        quiz_history.append("And you got it right! 🎇")
    else:  # if incorrect
        print("🧨 Wrong! Better luck next time! 🤡")
        quiz_history.append(f"And you guessed {guess[1]}... Wrong! 🧨")

    # quick spacing for history print later
    print()
    quiz_history.append("")

# end of quiz
print()
print("That's all for now, folks!")
print(f"You got {total_correct} out of {questions} right!")
print()

# check for history print
if yes_no("Would you like to read the quiz history? "):
    print()
    print("🎞 Quiz History! 🎞")
    for item in quiz_history:
        print(item)

print("Thank you for taking part in this experiment today!")
