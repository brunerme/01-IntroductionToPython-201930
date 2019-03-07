"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Maria Brunre.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()

turtle_1=rg.SimpleTurtle('turtle')
turtle_1.pen=rg.Pen('yellow',5)
turtle_1.speed=25
size=150
for k in range (12):
    turtle_1.draw_square(size)
    turtle_1.pen_up()
    turtle_1.right(50)
    turtle_1.forward(70)
    turtle_1.left(80)
    turtle_1.pen_down()


turtle_2=rg.SimpleTurtle('turtle')
turtle_2.pen=rg.Pen('orange',3)
turtle_2.speed=40
size2=100
for k in range(4):
    turtle_2.draw_square(size2)
    turtle_2.pen_up()
    turtle_2.backward(80)
    turtle_2.right(90)
    turtle_2.pen_down()

