from random import randint
print("I made up a number. Can you guess it?")
random_int = randint(1, 100)
char = int
while char != random_int:
    try:
        char = int(input("Enter integer: "))
        if char > random_int:
            print("Too high")
        elif char < random_int:
            print("Too low")
        else:
            print("Yay!")
    except:
        print("Wrong data! Please, enter an integer.")
