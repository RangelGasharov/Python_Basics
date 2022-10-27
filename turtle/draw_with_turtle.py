import turtle

tree_positions = ((50, 20), (80, 0), (120, -30), (150, -60), (190, -90))

window = turtle.Screen()
window.bgcolor("red")

tree = turtle.Turtle()
tree.penup()
tree.color("forest green")

trunk = turtle.Turtle()
trunk.color("brown")
trunk.right(90)
trunk.pensize(60)
trunk.penup()
trunk.forward(100)
trunk.pendown()
trunk.forward(250)


def make_tree_segment(size, top_position):
    tree.begin_fill()
    tree.setposition(0, top_position)
    tree.setposition(size, top_position-size)
    tree.setposition(-size, top_position-size)
    tree.setposition(0, top_position)
    tree.end_fill()


for size, top_position in tree_positions:
    make_tree_segment(size, top_position)

turtle.done()