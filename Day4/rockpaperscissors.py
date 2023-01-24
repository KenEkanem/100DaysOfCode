import random

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
game_images = [rock, paper, scissors]

user_sel = int(input("Please make a choice with '0' '1' or '2' \n"))
print(game_images[user_sel])

computer_sel = random.randint(0, 2)
print("computer: ")
print(game_images[computer_sel])


if user_sel >= 3 or user_sel < 0:
    print("you've selected an invalid number, You lose")
elif computer_sel > user_sel:
    print("You lose")
elif user_sel > computer_sel:
    print("you win")
elif computer_sel == user_sel:
    print("Its a draw!")
elif computer_sel == 0 and user_sel == 2:
    print("You lose!")