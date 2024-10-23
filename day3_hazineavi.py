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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n"
      "You are at a crossroad. Where do you wanna go?\n"
      , "     ", "Type 'left' or 'right'")

choice = input().lower()
if choice == "left":
    choice2 = input("You've come to a lake.\n"
                    "There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for the boat.\n"
                    "Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed.\n"
                        "There is a house with 3 doors.\n"
                        "One red, one yellow and one blue.\n"
                        "Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure. YOU WIN!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist.")
    else:
        print("You got attacked by an angry trout. Game over.")

else:
    print("You fell into a hole. Game over.")
