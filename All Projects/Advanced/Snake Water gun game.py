print("$$$ | SNAKE | WATER | GUN - GAME | $$$\n")

# Importing (RANDOM) module - line(3)
import random


def game_win(comp, you):  # Defining a function - line(7-24)
    if comp == you:  # Setting up conditions (Loosing, Winning or Match tie) - line(8-24)
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


print("Comp turn: Snake(s) Water(w) or Gun(g)")  # Printing game options - line(27)
randNo = random.randint(1, 3)  # Using (RANDOM) module - line(28)

# Setting up conditions (Computer's option selection) - line(30-36)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
else:
    comp = "g"

you = input("Your turn: Snake(s) Water(w) or Gun(g):-\t")  # Taking input from user - line(38)
print(f"\nComp choose: {comp} and you choose {you}\n")  # Printing selected options by Computer and User - line(39)
decision = game_win(comp, you)  # Using function call to call function - line(40)

# Setting up conditions (Decision making for result) - line(42-48)
if decision is None:
    print("The game is tie!")
elif decision:
    print("You win!")
else:
    print("You lose!")
