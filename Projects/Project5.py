import turtle, math, time, random
from utils import *

# Section 1: Setup
#  player character and any other sprites
s1 = create_sprite("Me4", 200,0)
s2 = create_sprite ("amelia", -200,0)
#  background
set_background ("CEC")
# starting value for your variables
sprite_list = []
s1_tags = 0
s2_tags = 0
who_is_it ="s1"
talker1 = create_sprite("alien", -250,200)
talker1.write(f"Amelia Tags:{s2_tags}",font = ("Arial", 40, "normal"))
talker1.hideturtle()
talker2 = create_sprite("alien", -250,150)
talker2.write(f"Penny Tags:{s1_tags}",font = ("Arial", 40, "normal"))
talker2.hideturtle()
# Section 2: Controls
# TODO - define your controls
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

def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 5
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 5
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 5
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 5
    y = s2.ycor() 
    s2.goto(x,y)
# TODO - pick keys for each control
window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_left2, "a")
window.onkeypress(move_right2, "d")

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions
    if get_distance(s1,s2) < 50:
        if who_is_it == "s1":
            s1_tags += 1
            who_is_it = "s2"
        elif who_is_it == "s2":
            s2_tags += 1
            who_is_it = "s1"
        s1.goto (200,0)
        s2.goto (-200,0)
    talker1.clear()
    talker1.write(f"Amelia Tags:{s2_tags}",font = ("Arial", 40, "normal"))
    talker2.clear()
    talker2.write(f"Penny Tags:{s1_tags}",font = ("Arial", 40, "normal"))
    # TODO - make an if statement for ending the game
    if i > 100*30:
        break

    time.sleep(0.01)
    window.update()
    

if s1_tags >= s2_tags:
    print("Penny gratefully wins")
if s2_tags > s1_tags:
    print("Amelia unfortunately wins")