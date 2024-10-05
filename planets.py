from planet import Planet
from constants import *

SUN = Planet(0, 0, 30, YELLOW, SUN_MASS)
SUN.sun = True

EARTH = Planet(-1 * AU, 0, 16, BLUE, EARTH_MASS)
EARTH.y_vel = 29.783 * 1000
MARS = Planet(-1.524 * AU, 0, 12, RED, MARS_MASS)
MARS.y_vel = 24.007 * 1000
MERCURY = Planet(0.387 * AU, 0, 8, DARK_GREY, MERCURY_MASS)
MERCURY.y_vel = -47.4 * 1000
VENUS = Planet(0.723 * AU, 0, 14, WHITE, VENUS_MASS)
VENUS.y_vel = -35.02 * 1000


