import pygame
from pygame.locals import *
import sys
# define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# initialize the work
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # if close clicked, quit and end program
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    window.fill(BLACK)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)



