name = input("Type your name: ")
print("Hello", name, "welcome to my Game!")

should_we_play = input("Do you want to play?(yes/no)   ").lower()

while should_we_play == "yes" or should_we_play == "y":
    print("Let's Begin!")
    weapon = input("Choose a weapon (axe/rope): ").lower()
    direction = input("Which way do you choose, left or right (left/right): ").lower()
    if direction == "left":
        if weapon == "rope":
            print("You crossed level 1 successfully!")
        else:
            print("Sorry you took the wrong step, YOU DIE..")
    elif direction == "right":
        print("You have crossed level 1 successfully")
    else:
        print("Sorry not a valid input, GAME OVER...")

    choice = input("Now there is a bridge. Do you want to cross it or swim under it? (cross/swim): ").lower()
    if choice == "swim":
        if weapon == "axe":
            print("YOU FOUND THE GOLD!! GAME OVER....")
        else:
            print("You are eaten by an alligator and GAME OVER...")
    else:
        print("YOU FOUND THE GOLD!! GAME OVER....")

    should_we_play = input("Do you want to play again? (yes/no): ").lower()
else:
    print("END....")
