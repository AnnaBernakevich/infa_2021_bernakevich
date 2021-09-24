import pygame
from pygame.draw import *
pygame.init()



FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (200, 100, 100), (0, 0, 400, 200)) #background

ellipse(screen, (120, 90, 60), (50, 30, 200, 80))

rect(screen, (100, 80, 0), (20, 100, 200, 200)) #body of the house

circle(screen, (250, 255, 250), (350, 50), 30)
rect(screen, (80, 10, 10), (30, 220, 50, 50))
rect(screen, (80, 10, 10), (95, 220, 50, 50))
rect(screen, (255, 255, 0), (160, 220, 50, 50))

rect(screen, (60, 60, 10), (40, 100, 25, 80))
rect(screen, (60, 60, 10), (85, 100, 25, 80))
rect(screen, (60, 60, 10), (130, 100, 25, 80))
rect(screen, (60, 60, 10), (175, 100, 25, 80))

circle(screen, (169, 169, 169), (320, 300), 20)
polygon(screen, (169, 169, 169), [(300, 300), (295, 340), (310, 350), (320, 345), (330, 340), (335, 340), (340, 350), (350, 330), (340, 300), (300, 310)])
circle(screen, (255, 0, 255), (310, 300), 5)
circle(screen, (255, 0, 255), (330, 300), 5)
circle(screen, (10, 0, 20), (310, 300), 5, 2)
circle(screen, (10, 0, 20), (330, 300), 5, 2)

polygon(screen, (30, 30, 10), [(10,100), (30,80), (210, 80),
                               (230,100), (10,100)])

ellipse(screen, (128, 0, 128), (150, 20, 200, 50))
ellipse(screen, (250, 128, 114), (80, 5, 200, 40))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()