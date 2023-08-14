## Conditional statements, Logical operators, code blocks and scope,ASCII Arts
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# code challenge
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
#
# else:
#     print("This is an odd number.")

## BMI calculator 2
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
#
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are slightly underweight")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have normal weight")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you  are slightly overweight")
# elif bmi < 35:
#     print(f"Your bmi is{bmi}, you are slightly obese")
# else:
#     print("You are clinically obese")

## This is a leap year calculator
# year = int(input("Which year do you want to check? "))
#
# if year % 4 != 0:
#     print("Not leap year")
# elif year % 100 != 0:
#     print("Leap year")
# elif year % 400 != 0:
#     print("Not leap")
# else:
#     print("leap yearear")

## This is a leap year calculator

# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# print("*" * 30)
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
# if size == "L":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}.")
# print("*\n" * 30)


## Treasure Island Game.
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision_1 = input("You\'re at a crossroad, where do you want to go, left or right? ")
if decision_1 == 'left':
    decision_2 = input(("Do you want to swim or wait? "))
    if decision_2 == 'wait':
        decision_3 = input("Which door do you want to open, Red, Yellow or Blue? ")
        if decision_3 == 'Yellow':
            print("You win!")
        elif decision_3 == 'Red' or 'Blue':
            print("Game Over!")
    else:
        print("Game over!")


else:
    print("Game Over!")
print("*\n" * 30)




