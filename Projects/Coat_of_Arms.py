# Section 1 - Your code
from utils import *
set_background("SUBX")

s1 = create_sprite("ukraine", 250, 115)
s2 = create_sprite("Milo2", -275, 115)
s3 = create_sprite("loom", -275, -115)
s4 = create_sprite("Me3", 275, -85)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Penny",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Life is Interesting",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()