from turtle import *

tracer(0)

koef = 20

right(45)
for i in range(7):
    forward(5 * koef)
    right(45)
    forward(10 * koef)
    right(135)



up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()
