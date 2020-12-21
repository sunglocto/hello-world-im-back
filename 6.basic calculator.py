import sys


def calc():
    num1 = input("Enter your first number.")
    num2 = input("Enter your second number.")
    try:
        result = int(num1) + int(num2)
    except:
        sys.exit("man i want whole numbers only not this shit")


    result = int(num1) + int(num2)
    print("The result was " + str(result))
    repeat = input("Do another calculation? (Y/N)")
    if repeat == "Y" or "y":
        calc()
    else:
        print("Terminating calculator. Thank you for using.")


print("This is a basic addition calculator.")
calc()