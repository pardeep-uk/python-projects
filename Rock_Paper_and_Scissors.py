import random
# Rock Paper Scissors ASCII Art
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock,Paper,Scissors]
your_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_value >= 3 or your_value < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[your_value])
    computer_value = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_value])
    if  your_value == 0 and computer_value == 2:
        print("You win!")
    elif your_value == 2 and computer_value == 0:
        print("You lose")
    elif computer_value > your_value:
        print("You lose")
    elif your_value == computer_value:
        print("It's a draw")
    elif your_value < computer_value:
        print("You win!")