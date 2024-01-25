from random import randint
from number_art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks answer against the guess. Returns number of attempts remaining."""
    
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")

def set_difficulty():
    """Sets the difficulty level"""
    
    level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def number_guessing_game():
    """The final game"""
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print("------------------------------------------------------------")
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("============================================================ \n")
            print("You've run out of guesses. You lose.")
            print(f"The correct asnwer was {answer}")
            return 

number_guessing_game()
