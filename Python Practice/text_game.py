#
#   Python 3.10.4
#
#   Author: Matthew Singleton (Under Tutorial from The Tech Academy)
#
#   Purpose:     The Tech Academy - Python Course. Creating our first program together.
#                Demonstrating how to pass variables from function to function while    
#                producing a functional game.
#
#

def start(nice=0, mean=0, name="Player 1"):
    #get the user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for 
        playing again and continue with our game.
    """
    # meaning, if we do not already have this user's name
    # then they are a new player and we need to get their name.
    if name != "Player 1":
        print("\nThank you for playing again, {}!".format(name))
    else: 
        stop = True
        while stop:
            if name == "Player 1":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean.")
                    print("\nHowever, at the end of the game, your fate \nwill be sealed by your actions. Choose carefully!")
                    stop = False
                else: 
                    print("Please enter a name.")
    return name

def nice_mean(nice,mean,name):           
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score() function 


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))
    
def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call the win function by passing in the variables needed
        win(nice,mean,name)
    if mean > 2: #Same, but for loss condition
        lose(nice,mean,name)
    else: #Otherwise, call nice_mean function passing in the variables so that it can use them.
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    # Substitute the {} wildcards with our var values
    print("\nNice job, {}. You won! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call the again function and pass in variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again> (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad. Sorry to see you go.")
            stop = False
            quit()
        else: 
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def lose(nice,mean,name):
     # Substitute the {} wildcards with our var values
    print("\n{}, you're an absolute MENACE! You lose! \nThe world has enough people like you \nand you should learn some manners!".format(name))
    #call the again function and pass in variables
    again(nice,mean,name)
    
def reset(nice,mean,name): 
    nice = 0
    mean = 0
    #Not resetting user's name since it's the same user.
    start(nice,mean,name)


if __name__ == "__main__":
    start()