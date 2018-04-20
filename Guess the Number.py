# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

secret_number = 0
number_of_guess = 0
current_range = 100

# helper function to start and restart the game
def new_game(max_number):
    # initialize global variables
    global secret_number
    global number_of_guess
    # set up number of attempts for different ranges
    if max_number == 100:
        number_of_guess = 7
    else:
        number_of_guess = 10
    # generate random number within the range
    secret_number = random.randrange(0,max_number)
    # print in the console new game statement
    print "New game. Range is from 0 to", max_number
    # print in the console number of remaining guess
    print "Number of remaining guess", number_of_guess
    return secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global current_range
    current_range = 100
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global current_range
    current_range = 1000
    new_game(1000)
    
def input_guess(guess):
    # main game logic 	
    global secret_number
    global number_of_guess
    global current_range
    int_number_guess = int(guess)
    print "Guess was", int_number_guess
    # compare guess number with selected number
    if int_number_guess>secret_number:
        print "Lower!"
    elif int_number_guess<secret_number:
        print "Higher!"
    else:
        print "Correct!!!"
        # after finishing one game the new game immediately starts
        new_game(current_range)
        # terminate input_guess function
        return
    # decrease number of guess
    number_of_guess = number_of_guess - 1
    # check number of attemps, if 0 end the game and start the new one
    if number_of_guess == 0:
        print "Game is over!!! New game is started immediately"
        new_game(current_range)
    else:
        # if number of attempts is not 0, print remaining number of attempts
        print "Number of remaining guess", number_of_guess    

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
inp=frame.add_button("Range is [0,100)", range100, 200)
inp=frame.add_button("Range is [0,1000)", range1000, 200)
inp=frame.add_input("Enter the guess", input_guess, 100)
frame.start()

# call new_game, start from [0;100] range
new_game(100)