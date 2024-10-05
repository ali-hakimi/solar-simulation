from planet import Planet
from constants import *

SUN = Planet(0, 0, 30, YELLOW, SUN_MASS)
SUN.sun = True

EARTH = Planet(-1 * AU, 0, 16, BLUE, EARTH_MASS)
MARS = Planet(-1.524 * AU, 0, 12, RED, MARS_MASS)
MERCURY = Planet(0.387 * AU, 0, 8, DARK_GREY, MERCURY_MASS)
VENUS = Planet(0.723 * AU, 0, 14, WHITE, VENUS_MASS)



