def hello(times, name):
    for i in range (times):
        print("Hi "+ name + "!")


ask = input("How many times shall the console say hi?")
ask = int(ask)
ask2 = input("What is their name?")
hello(ask, ask2)




