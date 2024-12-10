from tkinter import *
from constants import gravity, frame_rate
import math


class Cords:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Body:
    def __init__(self, canvas: Canvas, mass: float, center: Cords, color='grey'):
        self.velocity = 0
        self.center = center
        self.mass = mass

        radius = self.calcRadius(mass)
        self.radius = radius

        Ox = center.x
        Oy = center.y
        self.shape = canvas.create_oval(
            Ox - radius,
            Oy - radius,
            Ox + radius,
            Oy + radius,
            fill=color,
            outline="#004D40"
        )

    def calcRadius(self, mass: float):
        minRad = 10
        return max(minRad, mass/1000)

    def calcMovement(self, sun: 'Body'):
        dx = sun.center.x - self.center.x
        dy = sun.center.y - self.center.y
        hypotenuse = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        mx = self.velocity*dx/hypotenuse
        my = self.velocity*dy/hypotenuse
        self.center = Cords(self.center.x + mx, self.center.y + my)
        self.accelerate(sun)

        return Cords(mx, my)

    def collidesWith(self, sun: 'Body'):
        dx = sun.center.x - self.center.x
        dy = sun.center.y - self.center.y
        hypotenuse = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        return hypotenuse <= self.radius + sun.radius

    def accelerate(self, sun: 'Body'):
        dx = sun.center.x - self.center.x
        dy = sun.center.y - self.center.y
        distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        acceleration = gravity*(sun.mass / math.pow(distance, 2))
        self.velocity += acceleration*frame_rate*100000
        print(self.velocity)
