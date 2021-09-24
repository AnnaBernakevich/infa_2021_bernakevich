import pygame
from pygame.draw import *
pygame.init()


FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (250, 150, 10), (200, 200), 100)
circle(screen, (0, 0, 10), (150, 180), 10)
circle(screen, (0, 0, 10), (250, 180), 10)
polygon(screen, (160, 0, 10), [(150, 220), (250, 220), (220, 250), (180, 250)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()