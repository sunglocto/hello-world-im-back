def submit():
    if age == str(1):
        print("There was a man named " + name + ". He was " + str(age) + " year old. He really liked the name " + name + ", But didnt like being " + str(age) + ".")
    else:
        print("There was a man named " + name + ". He was " + str(age) + " years old. He really liked the name " + name + ", But didnt like being " + str(age) + ".")
age=70
name="George"
question1=input("Would you like to enter DEBUG MODE? (Y/N)")
if question1 == "Y":
    name1=input("What would you like the name to be? Currently: George.")
    age1 = input("What would you like the name to be? Currently: 70.")
    age=age1
    name=name1
    submit()
else:
    print("Entering normal mode.The Y needs to be uppercase to enter this mode!")
    submit()

#day 1 and 2