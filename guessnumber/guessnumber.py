# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui


# initialize global variables used in your code
secret_number = 0
range_number = 100
total_guesses = 7


# helper function to start and restart the game
def new_game():
    
    global secret_number, total_guesses
    secret_number = random.randrange(0, range_number)
    if (range_number == 100):
        total_guesses = 7
    elif (range_number == 1000):
        total_guesses = 10
    print ""
    print "New Game. Range is from 0 to ", range_number
    print "Number of remaining guesses is ", total_guesses
    


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restart
    global range_number, total_guesses
    range_number = 100
    total_guesses = 7
    print ""
    print "Range Changed to [0,100)"
    print "Number of remaining guesses is ",total_guesses
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global range_number
    range_number = 1000
    total_guesses = 10
    print ""
    print "Range Changed to [0,1000)"
    print "Number of remaining guesses is ",total_guesses
    new_game()
    
def input_guess(guess):
    number = int(guess)
    print ""
    print "Guess was", number
    global total_guesses    
    total_guesses = total_guesses - 1
    print "Number of remaining guesses is",total_guesses
    
    if (total_guesses == 0):
        print "You ran out of guesses. The number was", secret_number
        new_game()
        return
        
    if (number > secret_number) :
        print "Guess Lower"
    elif (number < secret_number) :
        print "Guess Higher"
    elif (number == secret_number):
        print "Correct Guess!"
        new_game()
    
        
def restart():
    new_game()

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)




# register event handlers for control elements
button1 = frame.add_button( "Range: 0-100", range100, 100)
button2 = frame.add_button( "Range: 0-1000", range1000, 100)
button3 = frame.add_button( " Restart", restart, 100)
input = frame.add_input('Take a Guess!', input_guess, 100)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
