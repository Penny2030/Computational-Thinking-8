import turtle, time, random
from utils import *

# Section 1 - Variables
x1 =-300
y1 =150
x2 =-300
y2 =-100
x3 =-300
y3 =200
x4 =-300
y4 =-250
x5 =-300
y5 =50

# Section 2 - Setup
set_background("Park")
t1 = create_sprite("Milo2",x1,y1)
t2 = create_sprite("Me4",x2,y2)
t3 = create_sprite("group (1)",x3,y3)
t4 = create_sprite("Me6",x4,y4)
t5 = create_sprite("Jasper2",x5,y5)


# Section 3 - Racing
for i in range(45):
    # Milo
    x1 += random.randint(12,20)
    # Me at starbucks
    x2 += 12
    # Friends
    x3 += 10
    # Other Me
    x4 += random.randint (10,18)
    # Jasper
    x5 += 7

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    t5.goto(x5, y5)
    window.update()
    time.sleep(0.1)
# Milo always wins because it has a higher chance of getting the higher random numbers than the other four sprites.  


# Section 4 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4 and x1 >= x5:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4 and x2 >= x5:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4 and x3 >= x5:
    print("Player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3 and x4 >= x5:
    print("Player 4 wins!")
elif x5 >= x1 and x5 >= x2 and x5 >= x4 and x5 >= x3:
    print("Player 5 wins!")

turtle.exitonclick()