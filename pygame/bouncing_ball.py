import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.slider import Slider
import sys
# define constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# initialize the work
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
X_SPEED = 5
Y_SPEED = 5
RADIUS = 10

x, y = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

while True:
    #window.fill(BLACK)
    for event in pygame.event.get():
        # if close clicked, quit and end program
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # default motion
    x += X_SPEED
    y += Y_SPEED
    pygame.draw.circle(window, RED, (x , y), RADIUS)

    # hits right wall
    if x + RADIUS >= WINDOW_WIDTH:
        X_SPEED = -X_SPEED
    # hits left wall
    if x - RADIUS <= 0:
        X_SPEED = -X_SPEED
    # hits floor
    if y + RADIUS >= WINDOW_HEIGHT:
        Y_SPEED = -Y_SPEED
    # hits ceiling
    if y - RADIUS <= 0:
        Y_SPEED = -Y_SPEED

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)