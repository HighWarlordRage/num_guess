#Title: Project-3c
print("Enter the integer for the player to guess.")
integer = int(input( ))
start = 0
print("Enter your guess.")
while(True):
    user_num = int(input())
    start = start + 1
    if user_num > integer:
        print("Too high - try again: ")
    elif user_num < integer:
        print("Too low - try again: ")
    else:
        print("You guessed it in",start,"tries.")


