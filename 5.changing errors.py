question = input("What is your favourite number?")
try:
    my_num = int(question)
except Exception:
    print("This ain't a whole number, dawg.")
try:
    print(str(my_num) + " is my favourite number!")
except Exception:
    print("😢")

