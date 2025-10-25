import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import sys
# define constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# slider sizing
slider_horizontal_padding = 25
slider_width = (WINDOW_WIDTH - slider_horizontal_padding * 4) // 2
slider_height = WINDOW_HEIGHT // 24
SLIDER_MIN = 1
SLIDER_MAX = 30
SLIDER_STEP = 1
SLIDER_PADDING = slider_height + 30
slider_y = 10
x_slider_x = slider_horizontal_padding
y_slider_x = slider_width + slider_horizontal_padding * 3

# initialize the work
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
X_SPEED = 5
Y_SPEED = 5
RADIUS = 10

x_slider = Slider(window, x_slider_x, slider_y, slider_width, slider_height, min=SLIDER_MIN, max=SLIDER_MAX, step=SLIDER_STEP)
y_slider = Slider(window, y_slider_x, slider_y, slider_width, slider_height, min=SLIDER_MIN, max=SLIDER_MAX, step=SLIDER_STEP)
x_label = TextBox(window, x_slider_x, slider_y, 60, 25, fontSize=15)
x_label.setText("X Speed")
y_label = TextBox(window, y_slider_x, slider_y, 60, 25, fontSize=15)
y_label.setText("Y Speed")

negative_y = False
negative_x = False

x, y = (WINDOW_WIDTH / 2, (WINDOW_HEIGHT - SLIDER_PADDING) / 2)

while True:

    # adjust speed according to slider
    if negative_x:
        X_SPEED = -x_slider.value
    else:
        X_SPEED = x_slider.value
    if negative_y:
        Y_SPEED = -y_slider.value
    else:
        Y_SPEED = y_slider.value


    window.fill(BLACK)
    events = pygame.event.get()
    for event in events:
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
    if y + RADIUS >= WINDOW_HEIGHT :
        Y_SPEED = -Y_SPEED
    # hits ceiling
    if y - RADIUS <= SLIDER_PADDING:
        Y_SPEED = -Y_SPEED

    # determine whether x and y is negative and boolean
    if Y_SPEED < 0:
        negative_y = True
    else:
        negative_y = False
    if X_SPEED < 0:
        negative_x = True
    else:
        negative_x = False

    pygame_widgets.update(events)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)