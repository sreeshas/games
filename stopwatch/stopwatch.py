# template for "Stopwatch: The Game"

import simplegui
# define global variables
second_counter = 0
stop_counter = 0
success_counter = 0

is_timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def second_interval_timer_handler():
    global second_counter
    second_counter = second_counter + 1;
    #print second_counter
    return

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(second_counter), (100, 100), 40, 'Red')
    canvas.draw_text(str(success_counter), (250, 20), 20, 'Green')
    canvas.draw_text("/" +str(stop_counter), (260, 20), 20, 'White')
    return

# define start timer handler
def start_timer_handler():
    global is_timer_running
    if (is_timer_running == True):
        return
    secondtimer.start()
    is_timer_running = True
    return
    
# define stop timer hander
def stop_timer_handler():
    global stop_counter, success_counter, is_timer_running
    if (is_timer_running == False):
        return
    stop_counter = stop_counter + 1
    secondtimer.stop()
    is_timer_running = False
    if (second_counter % 10 == 0):
        success_counter = success_counter + 1
    return

# define restart button handler
def reset_button_handler():
    global second_counter, stop_counter, success_counter, is_timer_running
   
    if (is_timer_running == True):
        secondtimer.stop()
        is_timer_running = False
    second_counter = 0
    stop_counter = 0
    success_counter = 0
    
    
# define format function
def format(ms):
    a = 0
    b = 0
    c = 0
    d = 0
    d = ms % 10
    seconds = ms /10 
    minute = seconds / 60
    a = minute
    lessthanminute = seconds % 60
    b = lessthanminute / 10
    c = lessthanminute % 10
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# create frame
frame = simplegui.create_frame('Timer', 300, 200)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw_handler)
startButton = frame.add_button('Start', start_timer_handler, 50)
stopButton = frame.add_button('Stop', stop_timer_handler, 50)
resetButton = frame.add_button('Reset', reset_button_handler, 50)
# register event handlers


# start frame
secondtimer = simplegui.create_timer(100, second_interval_timer_handler)
frame.start()

# Please remember to review the grading rubric

