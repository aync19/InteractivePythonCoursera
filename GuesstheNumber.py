import simplegui
import random
import math

# input will come from buttons and an input field
# all output for the game will be printed in the console



# initialize global variables used in your code

valueToGuess = -1
ran100 = True
numberOfGuesses = -1
guessedNumber = -1


# helper function to start and restart the game
def new_game():
    global ran100, valueToGuess, numberOfGuesses
    if ran100:
        maxNumber = 99
        valueToGuess = random.randrange(0, 100)
        numberOfGuesses = int(math.ceil(math.log(100, 2)))
        ran100 = True
    else:
        maxNumber = 999
        valueToGuess = random.randrange(0, 1000)
        numberOfGuesses = int(math.ceil(math.log(1000, 2)))
        ran100 = False
    print "Starting a new game!"
    print "Choose a number between 0 and", maxNumber
    print "You have", numberOfGuesses, "chances."
    print ""
    

# define event handlers for control panel
def range100():
    global ran100
    ran100 = True
    new_game()

def range1000():
    global ran100
    ran100 = False
    new_game()
    
def input_guess(guess):
    # main game logic
    global guessedNumber, numberOfGuesses;
    try:
        guessedNumber = int(guess);
    except ValueError:
        print guess, "is not an integer. Please try again."
        return
        
    if (ran100 and (guessedNumber < 0 or guessedNumber > 99)):
        print "The number", guessedNumber, "is out of range. Range is between 0 and 99 inclusive." 
    elif (not ran100 and (guessedNumber < 0 or guessedNumber > 999)):
        print "The number", guessedNumber, "is out of range. Range is between 0 and 999 inclusive." 
    if guessedNumber > valueToGuess:
        numberOfGuesses = numberOfGuesses - 1; 
        print "The number", guessedNumber, "is too high. You have", numberOfGuesses, "more chances."
        if numberOfGuesses == 0:
            print "You are out of chances. The correct number is ", valueToGuess
            print ("")
            new_game()
    elif guessedNumber < valueToGuess:
        numberOfGuesses = numberOfGuesses - 1 
        print "The number", guessedNumber, "is too low. You have", numberOfGuesses, "more chances."
        if numberOfGuesses == 0:
            print "You are out of chances. The correct number is ", valueToGuess
            print ""
            new_game()
    else:
        print "You guessed", guessedNumber,  "correctly!"
        print ""
        new_game()
       
                
    
    
# create frame

frame = simplegui.create_frame('Testing', 200, 300)


# register event handlers for control elements
frame.add_button('Range is [0-100)', range100, 125)
frame.add_button('Range is [0-1000)', range1000, 125)
frame.add_input('Guess a number', input_guess, 125)


# call new_game and start frame

new_game()
frame.start()
