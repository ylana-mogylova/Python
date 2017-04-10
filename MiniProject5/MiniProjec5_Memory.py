#http://www.codeskulptor.org/#user43_Mt6vZLu8nHeaREe_94.py


# implementation of card game - Memory

import simplegui
import random
IMAGE_HEIGHT = 100
IMAGE_WIDTH = 50
card_deck1 = []
card_deck_main = []
exposed = []
state = 0
index_exposed1 = 0
index_exposed2 = 0
turns = 0

green_card = simplegui.load_image("https://s3-us-west-2.amazonaws.com/ulianatest/CardGreen.png")
white_card = simplegui.load_image("https://s3-us-west-2.amazonaws.com/ulianatest/CardWhite.png")

for each in range(16):
    exposed.append(False)


# helper function to initialize globals
def new_game():
    global card_deck1
    global card_deck_main
    global exposed
    global state
    global index_exposed1
    global index_exposed2
    global turns
    
    card_deck1 = range(8)
    card_deck_main = card_deck1 * 2
    random.shuffle(card_deck_main)
    for each in range(16):
        exposed[each] = False
        
    state = 0
    index_exposed1 = 0
    index_exposed2 = 0
    turns = 0
    label_text = "Turns = " + str(turns)
    label.set_text(label_text)

     
# define event handlers
def mouseclick(pos):
    global state
    global index_exposed1
    global index_exposed2
    global card_deck_main
    global turns
        
    card_index = pos[0] // 50
    # check if card already exposed
    if exposed[card_index] != True: 
        if state == 0:
            state = 1
            exposed[card_index] = True
            index_exposed1 = card_index
        elif state == 1:
            state = 2

            exposed[card_index] = True
            index_exposed2 = card_index

            turns = turns + 1
            label_text = "Turns = " + str(turns)
            label.set_text(label_text)

        else:
            state = 1
            if card_deck_main[index_exposed1] != card_deck_main[index_exposed2]:
                exposed[index_exposed1] = False
                exposed[index_exposed2] = False
                exposed[card_index] = True
                index_exposed1 = card_index
            else:
                exposed[card_index] = True
                index_exposed1 = card_index
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    card_pos = [0, 0]
    
    for card_index in range(len(card_deck_main)):
        card_pos[0] = 2 * 25 * card_index + 25
        card_pos[1] = 60
        canvas.draw_text(str(card_deck_main[card_index]), card_pos, 30, "White")
    
    for i in range(16):
        if not exposed[i]:
            canvas.draw_image(green_card, (25, 50), (50, 100), ((2*25*i + 25), 50), (50, 100))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
