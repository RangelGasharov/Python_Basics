import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)

for i in range(24):
    for colours in ["blue", "green", "yellow", "orange", "red", "brown"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(2.5)
turtle.clear()

for i in range(24):
    for colours in ["blue", "green", "yellow", "orange", "red", "brown"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(-2.5)
turtle.done()


