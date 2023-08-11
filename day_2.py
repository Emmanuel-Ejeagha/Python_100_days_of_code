# Data Types, Numbers, Operators,Type Conversion, f-string
# print(123_323_432)
# print("Hello"[5])

# two_digit_number = input("Type a two-digit number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
#
# result = int(first_digit) + int(second_digit)
# print("Sum of = " + first_digit + " and " + second_digit)
# print(result)
# print(3 * (3 + 3) / 3 - 3)
#
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = int(weight) / float(height) ** 2
# my_bmi = int(bmi)
# print(my_bmi)

age = input("What is your current age? ")
age = int(age)
age = 90 * age
months = age * 12
weeks = age * 52
days = age * 365
print(f"You have {days} days, {weeks} weeks and {months} months left.\n")

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
tips = (tip / 100 * bill) + bill
people = int(input("How many people to split the bill? "))
total_bill = (tips / people)
payment = round(total_bill, 2)
print(f"Each person should pay: ${payment}")
