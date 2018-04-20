# template for "Stopwatch: The Game"
import simplegui
# define global variables
# interval is a timer interval of 0.1 of a second
interval = 0

# number of times when timer is stopped
number_attempts = 0

# number of times when timer is stopped 
# and tenth of a second is equal 0
you_won_number_attempts = 0

# A represents minutes in format A:BC.D
A = 0
# B represents seconds decimals in format A:BC.D
B = 0
# B represents seconds in format A:BC.D
C = 0
# B represents tenths of a second in format A:BC.D
D = 0

# global variable to define if timer is running
timer_running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A
    global B
    global C
    global D
    A = 0
    B = 0 
    C = 0
    D = 0
    # module of global interval always define D
    D = t % 10
    C = t / 10
    if C >= 10 and C < 60:
        B = (t / 10) / 10
        C = (t / 10) % 10
    elif C >= 60:
        A = (t / 10) / 60
        C = (t / 10) % 10
        B = ((t / 10) % 60) / 10
    # if A (minutes) is 10, stop the game by calling reset function
    if A == 10:
        formated_time = "Game is over"
        reset_button_handler()
        
    # return the result in format A:BC.D    
    formated_time = str(A)+":"+str(B)+str(C)+"."+str(D)
    return formated_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global timer_running
    timer_running = True
    timer1.start()

def stop_button_handler():
    global number_attempts
    global timer_running
    global you_won_number_attempts
    global D
    # check if tenth of second is equal 0
    # and timer is running
    if D==0 and timer_running:
        you_won_number_attempts = you_won_number_attempts + 1
        
    if timer_running:
        number_attempts = number_attempts + 1
        timer_running = False
    timer1.stop()

def reset_button_handler():
    global interval 
    global number_attempts
    global timer_running
    global you_won_number_attempts
    interval = 0
    timer_running = False
    number_attempts = 0
    you_won_number_attempts = 0
    timer1.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global interval
    interval = interval + 1
    #print interval

# define draw handler
def draw_handler(canvas):
    global number_attempts
    global you_won_number_attempts
    global interval
    canvas.draw_text(str(you_won_number_attempts) + " / " + str(number_attempts),(220,50), 30, 'Green')
    canvas.draw_text(format(interval), (100, 150), 45, 'White')
    return
    
# create frame
frame = simplegui.create_frame('Timer', 300, 300)
button_start = frame.add_button('Start', start_button_handler)
button_stop = frame.add_button('Stop', stop_button_handler)
button_reset = frame.add_button('Reset', reset_button_handler)
timer1 = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric