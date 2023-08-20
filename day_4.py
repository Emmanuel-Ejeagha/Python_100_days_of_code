# import random
#
# random_integer = random.randint(1, 20)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# if love_score == 6:
#     print(f"You scored the highest point {love_score}, you are deeply in love")
# elif love_score == 1:
#     print(f"Your love score is {love_score}, you are not in love")
# else:
#     print(f"your love score is {love_score}")

## Exercise 1
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#
# random_slide = random.randint(0, 1)
# if random_slide == 1:
#     print("Heads")
# else:
#     print("Tails")

# states_in_nigeria = ["Enugu", "Kano", "Lagos", "Rivers"]
# print(states_in_nigeria[-1])

## Exercise 2
# import random
#
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#
# namesAsCSV = input("Give me everybody's names, separated by a comma. ")
# names = namesAsCSV.split()
#
# random_choice = random.choice(names)
# print(random_choice + " is going to pay the bills")

# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#
# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split()
#
# names_index = len(names)
# random_selection = random.randint(0, names_index - 1)
# payer = names[random_selection]
# print(f"{payer} is going to pay the bills!")


# exercise 3
# row1 = ["⬜","⬜","⬜"]
# row2 = ["⬜","⬜","⬜"]
# row3 = ["⬜","⬜","⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
#
# print(f"1 {row1}\n2 {row2}\n3 {row3}")

# Exercise 4
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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    random_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[random_choice])

    if user_choice == 0 and random_choice == 2:
        print("You win!")
    elif random_choice == 0 and user_choice == 2:
        print("You lose!")
    elif random_choice == user_choice:
        print("It's a draw!")
    elif user_choice > random_choice:
        print("You win!")
    else:
        print("You lose!")

