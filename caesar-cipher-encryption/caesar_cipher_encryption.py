from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""  

  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
        
  print(f"Here's the {cipher_direction}d result: {end_text}")

      
should_continue = True
while should_continue:
    print("================================================================== \n")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")

    #check if the shift amount is integer or not
    try:
        shift = int(shift)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    shift = shift % 26

    #check if the direction value is correct or not
    if direction =="encode" or direction == "decode":
            caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("Invalid input! Please try again.")

    #asking user if they want to continue or not
    result = input("Type 'yes if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
    