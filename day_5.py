# # For Loops, Range, Code Blocks
# fruits = ["Pear", "Paw-Paw", "Mango", "Pineapple"]
# for fruit in fruits:
#     print(fruit)
# print(fruit + " is good for your body")

# Exercise 1 create a sum and len function
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# num_of_students = 0
# for student in student_heights:
#     num_of_students += 1
# print(num_of_students)
#
# average_height = total_height // num_of_students
# print(average_height)

## Exercise 2 create a max function
# student_scores = input("Input the list of students scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"The highest score in the class is: {max_score}")

## Exercise 3 Create a Fizz Buzz game
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)
#

## Exercise 4 Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


## Easy Level
# password = ""
# for leta in range(0, nr_letters):
#     password += random.choice(letters)
#
# for num in range(0, nr_symbols):
#     password += random.choice(numbers)
#
# for sym in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# print(password)

## Hard Level
my_passwd = []
for leta in range(0, nr_letters):
    my_passwd += random.choice(letters)

for num in range(0, nr_symbols):
    my_passwd+= random.choice(numbers)

for sym in range(0, nr_symbols):
    my_passwd += random.choice(symbols)

print(my_passwd)
random.shuffle(my_passwd)

generated_passwd = ""
for password in my_passwd:
    generated_passwd += password
print(f"Your password is: {generated_passwd}")
