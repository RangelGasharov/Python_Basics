import turtle
from turtle import *

turtle.title("Polygons")
speed(0)
bgcolor("black")
r, g, b = 255, 0, 0

for i in range(255 * 2):
    colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3

    fd(1 + i)
    rt(72)
    pencolor(r, g, b)

turtle.clear()
turtle.penup()
turtle.setposition(0, 0)

r, g, b = 0, 0, 0
turtle.pendown()
pencolor(r, g, b)

for i in range(255 * 2):
    colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r += 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r -= 3
    else:
        b -= 3

    fd(1 + i)
    rt(121)
    pencolor(r, g, b)

turtle.clear()
turtle.penup()
turtle.setposition(0, 0)

r, g, b = 100, 100, 100
turtle.pendown()
pencolor(r, g, b)

for i in range(255 * 2):
    colormode(255)
    fd(1 + i)
    rt(61)
    pencolor(r, g, b)

turtle.clear()
turtle.penup()
turtle.setposition(0, 0)

r, g, b = 200, 200, 200
turtle.pendown()
pencolor(r, g, b)

for i in range(255 * 2):
    colormode(255)
    fd(1 + i)
    rt(45)
    pencolor(r, g, b)
