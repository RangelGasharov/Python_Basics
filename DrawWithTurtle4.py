import turtle
from turtle import *
import math

turtle.title("Test")
bgcolor("black")

circle = turtle.Turtle()
circle.color("red")
circle.speed(10)

for i in range(500):
    circle.forward(math.sqrt(i))
    circle.left(i % 180)
