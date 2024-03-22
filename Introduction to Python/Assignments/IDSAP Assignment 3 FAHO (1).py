##########################################################################
# INSERT YOUR NAME AND ITU EMAIL ADDRESS HERE:
# NAME: "Frederik Aagot Oksbroe Holbech"
# ITU EMAIL ADDRESS: "faho@itu.dk"

##########################################################################
# IMPORTING MODULES
# import the random module needed
import random
# "seed" the random module with 42
random.seed(42)

##########################################################################
# DEFINING FUNCTIONS

# define a function that: 
# with the string "Rock, paper, scissors, worldpeace, or quit? (R, P, S, W, Q) ",
# prompts the user to input a letter;
# converts the user input into upper case by default;
# checks whether user input is an accepted value (R, P, S, W, or Q);
# and if not - keeps on asking the same question until input is an accepted value;
# finally, function returns the user input (in upper case)
def user_plays():

    # get input from user    
    # convert into uppercase
    while True:
        user_input = input("Rock, paper, scissors, worldpeace, or quit? (R, P, S, W, Q) ").upper()
        if user_input in ["R", "P", "S", "W", "Q"]:
            return user_input

    # (repeat same 2 steps from above, as long as needed)

    # return a valid user move

# define a function for the move made by the computer:
# each time the computer plays, randomly choose and return R/P/S 
# (computer will never want to quit, and never play worldpeace)
def computer_plays():
    return random.choice(["R", "P", "S"])

# define a function that evaluate two moves (both either R, P, or S)
# against each other and returns a string containing both moves and either 
# "you win", "computer wins", or "it's a tie"
def evaluate_moves(usermove, computermove):
    # if... (either it's a tie)
    if usermove == computermove:
        return f"User chose {usermove}, Computer chose {computermove}. It's a tie!"
    # elif... (or you won)
    elif(
        (usermove == "R" and computermove == "S")
        or (usermove == "P" and computermove == "R") 
        or (usermove == "S" and computermove == "P")
    ):
        return f"User chose {usermove}, Computer chose {computermove}. User wins!"
        
    # else... (or, in all other cases, you lose)
    else:
        return f"User chose {usermove}, Computer chose {computermove}. Computer wins!"

##########################################################################
# GAME STARTS

# Welcome message
print("Welcome to Rock, Paper, Scissors, Worldpeace!")
# eternal while loop
while True:
    # let user make a move (R, P, S, W, or Q) with the user_plays() function
    user_input = user_plays()
    # if user wants to quit, break out of the while 
    if user_input == "Q":
        print("Thank you for playing. Goodbye!")
        break
    # if user inputs "W" (or "w"), they immediately win
    if user_input == "W":
        print("User chose Worldpeace. User wins!")

    # else, we play a proper round of rock paper scissors: 
        # computer makes a move with the computer_plays() function,        
        # the moves are evaluated against each other with the evaluate_moves() function,
        # (we only have to consider the cases R, P, S for each)
        # show the result to the user
    else:
        computerchoice = computer_plays()
        result = evaluate_moves(user_input,computerchoice)
        print(result)
