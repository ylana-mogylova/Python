# Rock-paper-scissors-lizard-Spock template
import simplegui

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=="rock":
        choice_number = 0
    elif name=="Spock":
        choice_number = 1
    elif name=="paper":
        choice_number = 2
    elif name=="lizard":
        choice_number = 3
    elif name=="scissors":
        choice_number = 4
    else:
        print "Your name " + name + " is not in the list of supported choices"
    return choice_number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        choice_name = "rock"
    elif number==1:
        choice_name = "Spock"
    elif number==2:
        choice_name = "paper"
    elif number==3:
        choice_name = "lizard"
    elif number==4:
        choice_name = "scissors"
    else:
        print "Your number " + str(number) + " is not in the list of supported numbers"
    return choice_name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number)%5
    # use if/elif/else to determine winner, print winner message
    if (difference == 1) or (difference == 2):
        winner = "Player"
    elif (difference == 3) or (difference == 4):
        winner = "Computer"
    else:
        winner = "No one"
    print winner + " wins"
    return (winner)

# input handler
def player_choice(playerChoice):
    if (playerChoice not in ("rock", "Spock", "paper", "lizard", "scissors")):
       print "You enter not correct choice"
    else:
       rpsls(playerChoice) 

# create a frame with input field
frame = simplegui.create_frame("RPSLS", 200, 200)
inp = frame.add_input('Enter your choice', player_choice, 100)
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric

