# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
time_in_tenths = 0
number_of_successful_stops = 0;
number_of_total_stops = 0
is_running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t/600
    B = (t/100)%6
    C = (t%100)/10
    D = t%10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_but_handler():  
    global is_running
    timer.start()
    is_running = True
    
def stop_but_handler():
    global number_of_successful_stops, number_of_total_stops, is_running
    timer.stop()
    if(is_running == True):
        number_of_total_stops += 1
        if(time_in_tenths % 10 == 0):
            number_of_successful_stops += 1
    is_running = False
    
def reset_but_handler():
    global time_in_tenths, number_of_successful_stops, number_of_total_stops,is_running
    timer.stop()
    time_in_tenths = 0
    number_of_successful_stops = 0;
    number_of_total_stops = 0
    is_running = False
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_in_tenths
    time_in_tenths += 1
    #print time_in_tenths
    
# define draw handler
def draw_handler(canvas):
    show_string = str(number_of_successful_stops) + "/" + str(number_of_total_stops)
    canvas.draw_text(format(time_in_tenths), (60, 120), 20, 'White')
    canvas.draw_text(show_string, (190, 50), 24, 'White')

# create frame


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame = simplegui.create_frame('StopWatch', 250, 250)
frame.set_draw_handler(draw_handler)
button_start = frame.add_button('Start', start_but_handler)
button_stop = frame.add_button('Stop', stop_but_handler)
button_reset = frame.add_button('Reset', reset_but_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
