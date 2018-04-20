# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0, 0]
ball_vel = [-40.0 / 60.0,  5.0 / 60.0]
ball_vel = [1,3]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score_right_player = 0
score_left_player = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    # initial ball position in the middle of the canvas
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # generate random velocity
    random_horizontal = random.randrange(3, 6)
    random_vertical = random.randrange(2, 5) 
   
    # change ball velocity if direction is RIGHT
    if direction == RIGHT:
        ball_vel[0] = random_horizontal # x coordinate velocity
        ball_vel[1] = -random_vertical # y coordinate velocity
    
    # change ball velocity if direction is LEFT    
    if direction == LEFT:
        ball_vel[0] = -random_horizontal # x coordinate velocity
        ball_vel[1] = -random_vertical # y coordinate velocity
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_right_player, score_left_player  # these are ints
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [-40.0 / 60.0,  5.0 / 60.0]
    # start new game from bounching ball to the right
    spawn_ball(RIGHT)    
    score_right_player = 0
    score_left_player = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global BALL_RADIUS, HALF_PAD_HEIGHT, HEIGHT
    global paddle1_vel, paddle2_vel
    global score_right_player, score_left_player
    hit_paddle = False
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball position
    ball_pos[0] = ball_pos[0] + ball_vel[0] # x coordinate
    ball_pos[1] = ball_pos[1] + ball_vel[1] # y coordinate
    
    
    # draw ball 
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT) and (paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel <= HEIGHT): 
        paddle1_pos = paddle1_pos + paddle1_vel
        
    if (paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) and (paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel <= HEIGHT):
        paddle2_pos = paddle2_pos + paddle2_vel
        
    # draw paddles
    # draw left paddle
    canvas.draw_polygon([(0,(paddle1_pos - HALF_PAD_HEIGHT)),(PAD_WIDTH, (paddle1_pos - HALF_PAD_HEIGHT)),(PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)), (0, (paddle1_pos + HALF_PAD_HEIGHT))], 1, 'White', 'White')
    # draw right paddle
    canvas.draw_polygon([((WIDTH - PAD_WIDTH), (paddle2_pos-HALF_PAD_HEIGHT)), (WIDTH, (paddle2_pos - HALF_PAD_HEIGHT)), (WIDTH, (paddle2_pos + HALF_PAD_HEIGHT)), ((WIDTH - PAD_WIDTH), (paddle2_pos + HALF_PAD_HEIGHT))], 1, 'White', 'White')
    
    # determine whether paddle and ball collide   
    # hit the left paddle
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)) and (ball_pos[1] < (paddle1_pos + HALF_PAD_HEIGHT)) and (ball_pos[1] > (paddle1_pos - HALF_PAD_HEIGHT)):
        # increase velocity to 10% when ball hits the left paddle
        ball_vel[0] = - ball_vel[0] * 1.1
        hit_paddle = True
    
    # hit the right paddle
    if (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH) and (ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT) and (ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT):
        # increase velocity to 10% when ball hits the left paddle
        ball_vel[0] = - ball_vel[0] * 1.1
        hit_paddle = True
    
    # check if the ball touches/collides with the left and right gutters
    # touch the left gutter
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and not hit_paddle:
        score_right_player = score_right_player + 1
        spawn_ball(RIGHT)
    # touch the right gutter
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH and not hit_paddle:
        score_left_player = score_left_player + 1
        spawn_ball(LEFT)
    # hits the buttom
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # hits the top
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
     
    # draw scores
    canvas.draw_text(str(score_left_player), [(WIDTH/4), (HEIGHT/4)], 30, 'White')  
    canvas.draw_text(str(score_right_player), [(WIDTH/4*3), (HEIGHT/4)], 30, 'White')

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle1_vel + 1
        
    if key == simplegui.KEY_MAP["down"]:
        
        paddle2_vel = paddle2_vel + 1  
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    
    if key == simplegui.KEY_MAP["w"]:
        
        paddle1_vel = paddle1_vel - 1
        
    if key == simplegui.KEY_MAP["up"]:
        
        paddle2_vel = paddle2_vel - 1

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Reset', new_game, 50)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()