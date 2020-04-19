#A game of reflexes. Try and stop the timer when 
#the last digit is 0!

import simplegui
# define global variables
counter=0
x=0
y=0
D=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    A = t/600
    total = t/10
    seconds = total%60
    B = seconds/10
    C=seconds%10
    D=str(t)[-1]
    return str(A)+":"+str(B)+str(C)+"."+D
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    if timer.is_running():
        timer.stop()
        global x,y,D
        y+=1
        if int(D)==0:
            x+=1
def reset():
    timer.stop()
    global counter,x,y
    counter=0
    x=0
    y=0
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter+=1
# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter),[125,160],24,"Orange")
    canvas.draw_text(str(x)+"/"+str(y),[250,30],24,"Orange")
# create frame
frame = simplegui.create_frame("Stopwatch", 300,300)
timer = simplegui.create_timer(100, tick)
# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
