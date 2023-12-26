import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level):
    if level=="easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS 

def checked_answer(guessed_number , answer , attempts):
    if guessed_number<answer:
        print("your guess is too low ")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right ....the answer is {answer}")

def game():
    print(logo_art.logo)
    print("let me think of a number between 1 to 50 : ")
    answer=random.randint(1,50)
    level=input("Choose the level of difficulty...Type 'easy' or 'hard':").lower()
    attempts=set_difficulty(level)

    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} remainning attempts to guess the number")
        guessed_number=int(input("Guess a number:"))
        attempts=checked_answer(guessed_number , answer , attempts)
        if attempts==0:
            print("you have no chance right now ..you lose the game!")
            return
        elif guessed_number!=answer:
            print("try again")
game()