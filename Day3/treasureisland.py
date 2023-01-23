print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

stage_1 = input('You\'re at a cross road, Do you want to go "Left" or "Right"? ').lower()
if stage_1 == "left":
    stage2 = input('you\'ve come to a lake. there is an island in the middle of the lake. type "wait" to wait for a boat. type "Swim" to swim across.').lower()
    if stage2 == "wait":
        stage3 = input('You got to the the castle, Choose a "Red" "Blue" or "yellow" "door"').lower()
        if stage3 == "yellow":
            print("You win")
        elif stage3 == "blue":
            print("You got eaten by beasts. Game Over.")
        elif stage3 == "red":
            print("You got burnt! Game Over!")
        else:
            ("You choose a wrong option, Game over!")
    else:
        print('You got the attacked by an angry trout')
else:
    print("You fell into a hole. Game Over")
