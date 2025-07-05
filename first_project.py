name = input("Type your name: ")
print("Hello", name, "welcome to my Game!" )

should_we_play = input("Do you want to play? ").lower()

while should_we_play == "yes" or should_we_play == "y" :
    print("Lets Begin! ")
    weapon = input("choose a weapon (axe/rope) ").lower()
    direction = input("Which way do you choose,left or right(left/right) :").lower()
    if direction == "left" :
        if weapon == "rope" :
            print("You crossed level 1 succesfully! ")
        else :
            print("Sorry you took the wrong step,YOU DIE.. ")
    elif direction == "right" :
        choice = input("You crossed level 1 succesfully and now there is a bridge do you wonna cross it or do you want to swin under it?(Cross/swim) ")
        if choice == "swim" :
            if weapon == "axe":
                print("YOU FOUND THE GOLD!! GAME OVER.... ")
            else :
                print("You are eaten by an aligator and GAME OVER...  ")
        else :
            print("YOU FOUND THE GOLD!! GAME OVER.... ")
    else :
        print("Sorry not a valid input,GAME OVER... ")
    
    should_we_play = input("Do you want to play again? (yes/no) ").lower()
else :
    print("END....")