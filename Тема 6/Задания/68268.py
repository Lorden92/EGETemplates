from turtle import *
tracer(0)

koef=20

x = 2
forward((x+2)*koef)
for i in range(4):
    forward(x*koef)
    right(90)
    forward((x+2)*koef)
right(90)
forward(2*x*koef)
for i in range(4):
    right(90)
    forward((3*x-1)*koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x*koef, y*koef)
        dot(3)

for x in range(1, 100):
    if (x + x + 2)**2 + (3 * x - 1)**2 - (x + 2)*(2 * x) >= 1500:
        print(x)
        break

exitonclick()
