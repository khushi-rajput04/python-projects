rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

def game():
  choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

  if choice == 0:
    print(rock)
  elif choice == 1:
    print(paper)
  elif choice == 2:
    print(scissors)
  else:
    print("Invalid Input")

  seq = [rock, paper, scissors]
  random_choice = random.choice(seq)
  print("Computer chose: \n", random_choice)

  if choice == 0 and random_choice == paper:
    print("You lose")

  elif choice == 0 and random_choice == scissors:
    print("You win")
    
  elif choice == 1 and random_choice == scissors:
    print("You lose")

  elif choice == 1 and random_choice == rock:
    print("You win")

  elif choice == 2 and random_choice == rock:
    print("You lose")

  elif choice == 2 and random_choice == paper:
    print("You win")
    
  else:
    print("It's a tie")

game()

# Asking the user if they want to play again
repeat = True
while repeat:
  if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
    game()
  else:
    repeat = False