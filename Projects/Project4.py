import turtle, time, random
from utils import *
# The goal and purpose of this game is to click your stress away by getting the most money and happiness.
# Section 1
# Background
set_background("Mansion2")
# Three variables
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
# The space key is pressed and an image of a brand new penny appears, the amount of money and happiness each goes up by one.
# Second control
def get_money():
    global money
    global happiness
    money -= 1
    happiness -= 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite ("OldPenny2",x,y)
window.onkeypress (get_money,"p")
# The P key is pressed and an image of a old penny appears, the amount of money and happiness each goes down by one.
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
# The Q key is pressed and an image of me as a child appears, the amount of happiness goes up by hundred.


# Section 3 - game loop
window.listen()
for i in range(1000000000):
    talker1.clear()
    talker1.write(f"Money:{money}",font = ("Arial", 40, "normal"))
    talker2.clear()
    talker2.write(f"Happiness:{happiness}",font = ("Arial", 40, "normal"))

    time.sleep(0.01)
    window.update()