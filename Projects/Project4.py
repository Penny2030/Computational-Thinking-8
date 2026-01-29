import turtle, time, random
from utils import *

# Section 1 - setup
# Background
set_background("Mansion2")
# Create two variables
money = 0
oldmoney = 0
Me6 = 0
happiness = 0
talker1 = create_sprite("alien", -250,200)
talker1.write(f"Money:{money}",font = ("Arial", 40, "normal"))
talker1.hideturtle()
talker2 = create_sprite("alien", -250,150)
talker2.write(f"Happiness:{happiness}",font = ("Arial", 40, "normal"))
talker2.hideturtle()
# Section 2 - controls
# Defines an action
def get_money():
    global money
    global happiness
    money += 1
    happiness += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("Penny",x,y)
# Key for action
window.onkeypress (get_money,"space")
# Second control
def get_oldmoney():
    global oldmoney
    global happiness
    oldmoney += 1
    happiness -= 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("OldPenny2",x,y)
window.onkeypress (get_oldmoney,"p")
# Thrid control
def get_Me6():
    global Me6
    global happiness
    happiness += 100
    Me6 += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("Me6",x,y)
window.onkeypress (get_Me6,"q")


# Section 3 - game loop
window.listen()
for i in range(1000000000):
    talker1.clear()
    talker1.write(f"Money:{money}",font = ("Arial", 40, "normal"))
    talker2.clear()
    talker2.write(f"Happiness:{happiness}",font = ("Arial", 40, "normal"))

    time.sleep(0.01)
    window.update()