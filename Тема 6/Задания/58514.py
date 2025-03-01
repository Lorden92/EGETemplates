from turtle import *

tracer(0)

koef = 20

x = 1
for i in range(6):
    forward(x*koef)
    right(90)
    forward(7*koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)


