# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_number = 0
num_range = 100
number_of_guesses = math.ceil(math.log(num_range, 2))
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    global secret_number
    global number_of_guesses
    secret_number = random.randrange(0, num_range)
    number_of_guesses = int(math.ceil(math.log(num_range, 2)))
    print
    if(num_range == 100):
        print "New game. Range is [0,100)"
    elif(num_range == 1000):
        print "New game. Range is [0,1000)"
    print "Number of remaining guesses is",number_of_guesses
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    # remove this when you add your code    
    
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print
    # remove this when you add your code
    global number_of_guesses
    entered_number = int(guess)
    print "Guess was ", entered_number
    inp.set_text("")   #clears the input box
    number_of_guesses = number_of_guesses - 1
    print "Number of remaining guesses is", number_of_guesses
    if(entered_number < secret_number):
        print "Higher!"
    elif(entered_number > secret_number):
        print "Lower!" 
    elif(entered_number == secret_number):
        print "Correct!"
        new_game()
    else:
        print "I dont understand your guess"
    if(number_of_guesses) == 0:
        print "You ran out of guesses.  The number was", secret_number
        new_game()

    
# create frame
myFrame = simplegui.create_frame('Enter guess', 250, 250)
inp = myFrame.add_input('My label', input_guess, 100)
button1 = myFrame.add_button('Range is [0,100)', range100, 100)
button2 = myFrame.add_button('Range is [0,1000)', range1000, 100)

# register event handlers for control elements and start frame

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
