# Functions, While Loop, Indentation
def hcf(a, b):

    while b != 0:
        c = a
        a = b
        b = c % b
    return a


print("Enter two numbers and i will tell you there HCF")
num1 = int(input("First number: "))
num2 = int(input("Second Number: "))
print(hcf(num1, num2))
