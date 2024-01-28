from game_logo import logo, vs
from game_data import data
import random

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    
    def format(account):
        '''Takes the acoount data and returns the printable format.'''
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_desc}, from {account_country}."
    
    def check_answer(guess, a_followers, b_followers):
        '''Takes the users guess and followers count and returns if the guess is correct'''
        if a_followers > b_followers:
            return guess == 'A'
        else:
            return guess == 'B'
    
    # generates random data for account A and account B
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)} \n")

    # Ask the user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Fetch the followers count of each account from the data
    a_followers_count = account_a['follower_count']
    b_followers_count = account_b['follower_count']
    
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # Displays if the answer is correct or wrong, also displays the score
    if is_correct:
        score += 1
        print("-------------------------------------------")
        print(f"You got it right! Current score: {score}")
        print("-------------------------------------------")

    else:
        game_should_continue = False
        print("-------------------------------------------")
        print(f"Sorry, that's wrong. Final score: {score}")
        print("-------------------------------------------")

    