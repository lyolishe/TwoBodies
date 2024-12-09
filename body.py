from tkinter import *
from constants import move_per_frame
import math


class Cords:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Body:
    def __init__(self, canvas: Canvas, mass: float, center: Cords, color='grey'):
        self.center = center
        Ox = center.x
        Oy = center.y
        radius = self.calcRadius(mass)
        self.radius = radius
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

    def calcMovement(self, sunCenter: Cords):
        dx = sunCenter.x - self.center.x
        dy = -self.center.y + sunCenter.y
        hypotenuse = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        mx = move_per_frame*dx/hypotenuse
        my = move_per_frame*dy/hypotenuse
        self.center = Cords(self.center.x + mx, self.center.y + my)
        return Cords(mx, my)

    def collidesWith(self, sun: 'Body'):
        dx = sun.center.x - self.center.x
        dy = -self.center.y + sun.center.y
        hypotenuse = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        return hypotenuse <= self.radius + sun.radius



