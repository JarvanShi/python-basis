import turtle
import math
turtle.setup(800, 800*(math.sqrt(5)-1)/2)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(25)
turtle.color('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 40)
turtle.fd(80)
turtle.circle(16, 180)
turtle.fd(80*2/3)
turtle.done()