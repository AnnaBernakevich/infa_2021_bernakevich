import pygame
import random
from pygame.draw import *
pygame.init()



FPS = 30
screen = pygame.display.set_mode((600, 700))

rect(screen, (200, 100, 100), (0, 0, 600, 300)) #background
circle(screen, (250, 255, 250), (350, 50), 30) #moon
ellipse(screen, (25, 25, 112), (250, 150, 400, 90))  # cloud_0

for i in range(3):
    k = (1-i/8)
    n = random.random()
    rect(screen, (100*n, 80*n, 0), (20 + 150*i, 400 - 100*i, 200, 200)) #body of the house

    rect(screen, (80, 10, 10), (30 + 150*i, 520 - 100*i, 50, 50)) #window_d
    rect(screen, (80, 10, 10), (95 + 150*i, 520 - 100*i, 50, 50)) #window_d
    rect(screen, (255, 255, 0), (160 + 150*i, 520 - 100*i, 50, 50)) #window_d

    rect(screen, (60, 60, 10), (40 + 150*i, 400 - 100*i, 25, 80)) #window_u
    rect(screen, (60, 60, 10), (85 + 150*i, 400 - 100*i, 25, 80)) #window_u
    rect(screen, (60, 60, 10), (130 + 150*i, 400 - 100*i, 25, 80)) #window_u
    rect(screen, (60, 60, 10), (175 + 150*i, 400 - 100*i, 25, 80)) #window_u
    polygon(screen, (30, 30, 10), [(10 + 150*i, 400 - 100*i), (30 + 150*i, 380 - 100*i), (210 + 150*i, 380 - 100*i),
                                   (230 + 150*i, 400 - 100*i), (10 + 150*i, 400 - 100*i)])  # roof

for i in range(10):
    dx = random.randint(10, 450)
    dy = random.randint(10, 300)
    k = random.random()
    circle(screen, (169, 169, 169), (120 + dx, 300 + dy), 20) #spook_head
    polygon(screen, (169, 169, 169), [(100 + dx, 300 + dy), (95 + dx, 340 + dy), (110 + dx, 350 + dy), (120 + dx, 345 + dy),
                                      (130 + dx, 340 + dy), (135 + dx, 340 + dy), (140 + dx, 350 + dy), (150 + dx, 330 + dy), (140 + dx, 300 + dy), (100 + dx, 310 + dy)]) #spook_body
    circle(screen, (255*(1-k), 0, 255), (110 + dx, 300 + dy), 5) #spook_eye_1
    circle(screen, (255*(1-k), 0, 255), (130 + dx, 300 + dy), 5) #spook_eye_2
    circle(screen, (10, 0, 20), (110 + dx, 300 + dy), 5, 2) #spook_eye_edge_1
    circle(screen, (10, 0, 20), (130 + dx, 300 + dy), 5, 2) #spook_eye_edge_2


for i in range(8):
    k = random.random()
    ellipse(screen, (170, 30, 150), (0, 50, 700 * (1 - k), 100 * k))  # cloud_1
    ellipse(screen, (128, 0, 128), (0, 90, 500*(1-k), 80*k)) #cloud_2
    ellipse(screen, (250, 128, 114), (0, 150, 600*(1-k), 80*k)) #cloud_3



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()