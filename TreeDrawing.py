from turtle import *
from random import randint

speed(0)


def draw_branch(len):
    if (len > 5):
        color("brown")
        forward(len)
        right(25)
        draw_branch(len - randint(4, 10))
        left(50)
        draw_branch(len - randint(4, 10))
        right(25)
        color("brown")
        backward(len)
    else:
        color("green", "green")
        begin_fill()
        circle(10 + randint(0, 5))
        end_fill()


def draw_tree(start_len):
    pendown()
    setheading(90)
    color("brown")
    pensize(5)
    draw_branch(start_len)


penup()
goto(-100, -200)
draw_tree(randint(40, 60))
penup()
goto(100, -180)
draw_tree(randint(30, 40))

#https://www.codheadz.com/2019/06/30/Trees-with-Turtle-in-Python/
