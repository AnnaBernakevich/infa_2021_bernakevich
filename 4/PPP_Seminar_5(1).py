import pygame
import random
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

def draw_sky(screen, color):
    '''
    function draws the sky on the screen
    screen - pygame.Surface object
    color - RGD-color of the sky
    '''
    rect(screen, color, (0, 0, 400, 200))

def draw_house(screen):
    '''
    function draws a house on the screen
    screen - pygame.Surface object
    '''
    rect(screen, (100, 80, 0), (20, 100, 200, 200)) #draw the body of the house
    draw_lower_windows(screen)
    draw_upper_windows(screen)
    draw_roof(screen)
    pass

def draw_moon(screen, r):
    '''
    function draws a moon on the screen
    r - radius of the moon
    screen - pygame.Surface object
    '''
    circle(screen, (250, 255, 250), (350, 50), r)
    pass

def draw_lower_windows(screen):
    '''
    function draws the lower windows of the house
    screen - pygame.Surface object
    '''
    rect(screen, (80, 10, 10), (30, 220, 50, 50)) #1st window
    rect(screen, (80, 10, 10), (95, 220, 50, 50)) #2d window
    rect(screen, (255, 255, 0), (160, 220, 50, 50)) #3d window
    pass

def draw_upper_windows(screen):
    '''
    function draws the upper windows of the house
    screen - pygame.Surface object
    '''
    rect(screen, (60, 60, 10), (40, 100, 25, 80)) #1st window
    rect(screen, (60, 60, 10), (85, 100, 25, 80)) #2d window
    rect(screen, (60, 60, 10), (130, 100, 25, 80)) #3d window
    rect(screen, (60, 60, 10), (175, 100, 25, 80)) #4th window
    pass

def draw_spook(screen):
    '''
    function draws the spook on the screen
    screen - pygame.Surface object
    '''
    circle(screen, (169, 169, 169), (320, 300), 20) #draw the head of the spook
    polygon(screen, (169, 169, 169), [(300, 300), (295, 340), (310, 350), (320, 345), \
                    (330, 340), (335, 340), (340, 350), (350, 330), (340, 300), (300, 310)]) #draw the body of the spook
    draw_eye(screen, 310, 300, 5) #draw the left eye of the spook
    draw_eye(screen, 330, 300, 5)  # draw the right eye of the spook
    pass

def draw_eye(screen, x, y, r):
    '''
    function draws the eye
    screen - pygame.Surface object
    x, y - coordinates of the eye
    r - radius of the eye
    '''
    circle(screen, (255, 0, 255), (x, y), r) #draw the eye
    circle(screen, (10, 0, 20), (x, y), r, 2)  # draw the boundary of the eye
    pass

def draw_roof(screen):
    '''
    function draws the roof of the house
    screen - pygame.Surface object
    '''
    polygon(screen, (30, 30, 10), [(10,100), (30,80), (210, 80),
                               (230,100), (10,100)])
    pass

def draw_clouds(screen):
    '''
    function draws the clouds on the screen
    screen - pygame.Surface object
    '''
    for i in range(8):
        k = random.random()
        ellipse(screen, (170, 30, 150), (0, 50, 700 * (1 - k), 80 * k))  # 1st cloud
        ellipse(screen, (128, 0, 128), (0, 90, 500 * (1 - k), 60 * k))  # 2d cloud
        ellipse(screen, (250, 128, 114), (0, 150, 600 * (1 - k), 60 * k))  # 3d cloud
    pass

draw_sky(screen, (200, 100, 100))
draw_moon(screen, 15)
draw_clouds(screen)
draw_house(screen)
draw_spook(screen)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()