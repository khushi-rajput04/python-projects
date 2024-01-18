from treasure_logo import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n")

lfirst = first.lower()

if lfirst == 'left':
  second = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
  
  lsecond = second.lower()
  
  if lsecond == 'wait':
    third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
    lthird = third.lower()
    if lthird == 'red':
      print("Burnt by fire. Game over.")
    elif lthird == 'blue':
      print("Eaten by beasts. Game over.")
    elif lthird == 'yellow':
      print("You found the treasure! You Win!")
    else:
      print("Game over.")

  else:
    print("Attacked by Crocodiles. Game over.")
    
else:
  print("Fell into a hole. Game over.")