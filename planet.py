from constants import *
import pygame

class Planet:

    def __init__(self, x, y, raduis, color, mass):
        self.x = x
        self.y = y
        self.radius = raduis
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x,y), self.radius)
