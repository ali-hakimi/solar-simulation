import pygame
import math
from planets import *
from constants import *
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("solar simulation")

def main():
    run = True
    clock = pygame.time.Clock()

    planets = [SUN, EARTH, MARS, MERCURY, VENUS]

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