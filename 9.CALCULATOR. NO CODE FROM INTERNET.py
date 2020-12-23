
import sys

def calc():
    operation1 = input("What is your operation?(X for multiplication, D for division, A for Addition and S for subtraction)")
    num1 = input("What is your first number?")
    num1 = float(num1)
    num2 = input("What is your second number?")
    num2 = float(num2)
    if operation1 == "X":
        answer = num1 * num2
    elif operation1 == "D":
        answer = num1 / num2
    elif operation1 == "S":
        answer = num1 - num2
    elif operation1 == "A":
        answer = num1 + num2
    else:
        sys.exit("Please try again as the operation you entered is not valid.")
    print("The answer is " + str(answer))
    request = input("Would you like to do another calculation? (Y)")
    if request == "Y":
        calc()
    elif request == "y":
        calc()
    else:
        sys.exit("Thank you for using the calculator.")

calc()




