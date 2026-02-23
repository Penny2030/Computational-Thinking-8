import time, turtle, random
from utils import *
# Section 1: Setup
s1 = create_sprite("Me6",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 5
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 5
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 5
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 5
    y = s1.ycor() 
    s1.goto(x,y)



# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")
def draw ():
    s1.pendown()
window.onkeypress(draw, "c")

def stop_drawing():
    s1.penup()
window.onkeypress(stop_drawing,"x")

def erase():
    s1.clear()
window.onkeypress(erase,"e")

def red_pen():
    s1.color("red")
window.onkeypress(red_pen,"r")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen,"g")

def reset():
    s1.goto(0,0)

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()