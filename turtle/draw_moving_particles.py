import math
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
        self.particle_turtle.pendown()

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

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.particle_turtle.goto(self.x, self.y)


class ParticleEquilateralPolygon:
    def __init__(self, center_x, center_y, path_side_length, movement_speed, amount_of_sides, particle_size,
                 color="#FFFFFF"):
        self.center_x = center_x
        self.center_y = center_y
        self.x = center_x
        self.y = center_y
        self.path_side_length = path_side_length
        self.particle_size = particle_size
        self.amount_of_sides = amount_of_sides
        self.speed = movement_speed
        self.color = color
        self.index_current_target_point = 0
        self.target_points = []
        angle_sector = 2 * math.pi / amount_of_sides
        radius = (self.path_side_length / 2) / math.sin(angle_sector / 2)

        for i in range(amount_of_sides):
            self.target_points.append(
                [math.sin(i * angle_sector) * radius + self.center_x,
                 math.cos(i * angle_sector) * radius + self.center_y])
        self.particle_turtle = turtle.Turtle()
        self.particle_turtle.shape("circle")
        self.particle_turtle.color(self.color)
        self.particle_turtle.penup()
        self.x = self.target_points[0][0]
        self.y = self.target_points[0][1]
        self.particle_turtle.goto(self.x, self.y)
        self.particle_turtle.shapesize(stretch_wid=self.particle_size, stretch_len=self.particle_size)
        self.particle_turtle.pendown()

    def animate(self):
        target_x = self.target_points[self.index_current_target_point][0]
        target_y = self.target_points[self.index_current_target_point][1]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance < self.speed:
            self.x = target_x
            self.y = target_y
            self.index_current_target_point = (self.index_current_target_point + 1) % self.amount_of_sides
        else:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

        self.particle_turtle.goto(self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Partikel im Rechteck")
screen.setup(width=600, height=600)
turtle.speed(0)

particle_1 = ParticleEquilateralPolygon(400, 200, 200, 7, 4, 0.5, "#80AF25")
particle_2 = ParticleEquilateralPolygon(0, -200, 200, 5, 4, 0.5, "#F32F8D")
particle_3 = Particle(particle_1.x, particle_2.y, 0, 0, 0, .5, "#B4DD1E")

while True:
    particle_3.set_position(particle_1.x, particle_2.y)
    particle_1.animate()
    particle_2.animate()
    screen.update()
