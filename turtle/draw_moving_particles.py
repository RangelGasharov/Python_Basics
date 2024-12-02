import turtle


class Particle:
    def __init__(self, start_x, start_y, path_width, path_height, speed, size,
                 color="#FFFFFF", direction_number=1):
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.path_width = path_width
        self.path_height = path_height
        self.speed = speed
        self.size = size
        self.color = color
        self.direction_number = direction_number

        self.particle_turtle = turtle.Turtle()
        self.particle_turtle.shape("circle")
        self.particle_turtle.color(self.color)
        self.particle_turtle.penup()
        self.particle_turtle.goto(self.x, self.y)
        self.particle_turtle.shapesize(stretch_wid=self.size, stretch_len=self.size)

    def animate(self):
        if self.direction_number == 1:
            self.x += self.speed
            if self.x >= self.path_width + self.start_x:
                self.direction_number = 2
        elif self.direction_number == 2:
            self.y -= self.speed
            if self.y <= self.start_y - self.path_height:
                self.direction_number = 3
        elif self.direction_number == 3:
            self.x -= self.speed
            if self.x <= self.start_x:
                self.direction_number = 4
        elif self.direction_number == 4:
            self.y += self.speed
            if self.y >= self.start_y:
                self.direction_number = 1

        self.particle_turtle.goto(self.x, self.y)


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Partikel im Rechteck")
screen.setup(width=600, height=600)

particle_1 = Particle(0, 0, 100, 100, 2, .5, "#FFFFFF")
particle_2 = Particle(100, 100, 100, 100, 2, .5, "#1AA8F9")

while True:
    particle_1.animate()
    particle_2.animate()
    screen.update()
