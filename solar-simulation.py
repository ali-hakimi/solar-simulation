import pygame
import math
from planet import Planet
from constants import *
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("solar simulation")

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, SUN_MASS)
    sun.sun = True

    planets = [sun]

    while run:
        clock.tick(60)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()

    
    pygame.quit()

main()