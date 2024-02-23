# Functions, While Loop, Indentation
def hcf(x, y):

    while y != 0:
        z = x
        x = y
        y = z % y
    return x


print("Enter two numbers and i will tell you there HCF")
num1 = int(input("First number: "))
num2 = int(input("Second Number: "))
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {result} ")