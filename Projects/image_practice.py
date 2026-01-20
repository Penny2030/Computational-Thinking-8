# Section 1 - Your code
from utils import *
set_background("moon")

s2 = create_sprite ("Milo", -100, 100)
s1 = create_sprite ("group",100,-100)
message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("kitten in space",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()