#Use buttons to increase and decrease the size of the circle
#Change color with input field
import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20
color = "Orange"

# Draw handler
def draw(canvas):
    global ball_radius
    canvas.draw_circle([200,200],ball_radius, 2, color)
# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius+=RADIUS_INCREMENT
    
def decrease_radius():
    global ball_radius
    if(ball_radius>RADIUS_INCREMENT):
        ball_radius-=RADIUS_INCREMENT
        
def circ_color(col):
    global color
    color = col

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius, 100)
frame.add_button("Decrease radius", decrease_radius, 100)
frame.add_input("Circle color", circ_color, 100)

# Start the frame animation
frame.start()

