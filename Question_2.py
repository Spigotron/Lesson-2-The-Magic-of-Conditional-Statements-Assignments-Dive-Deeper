num1 = int(input("Enter a number. "))
num2 = int(input("Enter a second number. "))
num3 = int(input("Enter a third number. "))

if num1 <= num2 <= num3 or num2 <= num1 <= num3:
    print("The largest number is", num3)
elif num1 <= num3 <= num2 or num3 <= num1 <= num2:
    print("The largest number is", num2)
elif num3 <= num2 <= num1 or num2 <= num3 <= num1:
    print("The largest number is", num1)

if num1 <= num2 <= num3 or num1 <= num3 <= num2:
    print("The smallest number is", num1)
elif num2 <= num3 <= num1 or num2 <= num1 <= num3:
    print("The smallest number is", num2)
elif num3 <= num2 <= num1 or num3 <= num1 <= num2:
    print("The smallest number is", num3)

if num1 == num2 == num3:
    print("All three of the numbers are equal!")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Two of the numbers are equal.")