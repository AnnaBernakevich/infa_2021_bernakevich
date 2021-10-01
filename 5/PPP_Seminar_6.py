import pygame
import numpy as np
import random
from pygame.draw import *

pygame.init()

# добавление таймера
clock = pygame.time.Clock()

# задание частоты и ширины/высоты открываемого экрана картинки
fps = 5
width = 600
height = 600


# задание цветов
black = (0, 0, 0)
blue = (0, 20, 140)
rama = (150, 150, 150)
grey = (192, 192, 192)
brown = (153, 76, 0)
green = (0, 204, 0)
darkgreen = (50, 100, 0)
darkbrown = (102, 51, 0)
darkgrey = (96, 96, 96)
darkblue = (50, 50, 100)


screen = pygame.display.set_mode((width, height))


def window(x, y, size, color):
    '''
    Рисует окно.
    x и y задают координаты верхнего левого угла окна.
    size - это ширина окна.
    '''
    rect(screen, rama, (x, y, size, size*2+size/40))
    rect(screen, color, (x + size / 10, y + size / 10, 4 * size / 5, 9 * size / 5))
    line(screen, rama, [x + size/2, y], [x+size/2, y+2*size], int(size/20))
    line(screen, rama, [x, y+2*size/3], [x+size-size/20, y + 2 * size/3], int(size/20))
    '''
    Сам код - чисто расчет для данногй модели окна
    '''

def legs(x, y, size, color):
    '''
    Рисует ноги кота.
    x и y - это координаты центра головы кота.
    size - это ширина туловища кота.
    color - это цвет ног кота.
    '''
    for z in 0.1 * size, 0.8 * size, 2 * size, 2.8 * size:
        polygon(screen, color, [(x + z, y + size / 2), (x + z + size / 4, y + size / 2 + size / 2), \
                                    (x + z, y + size / 2 + size), (x + z + size / 4, y + size / 2 + size / 2),
                                    (x + z, y + size / 2)], 13) # продолговатая часть ног
        ellipse(screen, color, (x + z - size / 5, y + size / 2 + 0.9 * size, 2 * size / 5, size / 5)) # ступни ног

def whiskers(x, y, size):
    '''
    Рисует усы кота.
    x и y - это координаты центра головы кота.
    size - это ширина туловища кота.
    '''
    for z in -size/4, size/4:
        for s in 0, size/8, -size/8:
            line(screen, black, (x+z, y+s+size/3), (x+2*z, y+2*s+size/3), 2)

def eyes(x, y, size):
    '''
    Рисует глаза кота.
    x и y - это координаты центра головы кота.
    size - это ширина туловища кота.
    '''
    for z in size/6, -size/6-size/5:
        ellipse(screen, blue, (x+z, y-size/4, size/5, size/8))

def ears(x, y, size, color):
    '''
    Рисует уши кота.
    x и y - это координаты центра головы кота.
    size - это ширина туловища кота.
    color - это цвет ушей кота.
    '''
    for z in -size/4, size/4:
        ellipse(screen, color, (x+1.4*z-x/15, y-1.5*size, size/3, 1.1*size))

def cat(x, y, size, color1, color2):
    '''
    Рисует кота.
    x и y задают координаты центра головы.
    size - это ширина туловища.
    color1 - это цвет для туловища и ушей.
    color2 - это цвет для головы, ног и хвоста.
    '''

    ellipse(screen, color1, (x, y, 3 * size, size))  # туловище
    circle(screen, color2, (x, y), 4 * size / 5)  # голова
    ellipse(screen, color2, (x+2.8*size, y, 1.5*size, size/2))  # хвост
    line(screen, black, (x, y), (x, y + size / 5), 3)  # нос
    line(screen, black, (x - size / 10, y + size / 3), (x + size / 10, y + size / 3))  # рот

    legs(x, y, size, color2)  # ноги
    eyes(x, y, size) # глаза
    ears(x, y, size, color1) # уши
    whiskers(x, y, size) # усы

    '''
    код - чисто расчет для данной модели кота
    '''

def ooo(x, y, size, color, bool):
    '''
    Рисует клубок x и y - это координаты центра клубка.
    size - это диаметр клубка.
    color - это цвет клубка.
    bool - в какую сторону повёрнута чёрная нитка от клубка (True - направо, False - налево)).
    '''
    # рисует рандомно торчащие цветные нитки:
    for i in range(10):
        Сolor = list(np.random.choice(range(256), size=3)) # рандомный цвет нитки
        n = random.random() # рандомное число для генерации положения нитки
        phi = 2 * np.pi * n # угол, характеризующий направление нитки
        x0 = size * np.sin(phi) # смещение начала нитки относ. центра клубка по оси х
        y0 = size * np.cos(phi) # смещение начала нитки относ. центра клубка по оси y
        arc(screen, Сolor, (x + x0 - 0.7 * size, y + y0 - 0.7 * size, 1.5 * size, 1.5 * size), phi, phi + np.pi)

    circle(screen, color, (x, y), size) # клубок

    # рисует чёрную нитку сбоку от клубка:
    if bool:
        arc(screen, black, (x+size/2**0.5, y+size/2.5, size, size), 0, 2.50)
        arc(screen, black, (x + 2.4*size / 2 ** 0.5, y + size / 2.2, size, size), 3, 6)
    else:
        arc(screen, black, (x - 2.7*size , y + size / 2.5, size, size), -2.5, 0)
        arc(screen, black, (x - 2.4 * size / 2 ** 0.5, y + size / 2.2, size, size), -6, -3)

    # рисует чёрные нитки внутри клубка:
    arc(screen, color, (x - size/3, y - size/2, size, size/2), 0, 2)
    arc(screen, color, (x - size / 2, y - size / 5, size, size), 2, 4)
    arc(screen, color, (x - size / 4, y - size / 4, size, size), 4, 6)


# разделение экрана на две части с разными цветами
rect(screen, darkblue, (0, 0, width, height/2))
rect(screen, darkgreen, (0, height/2, width, height/2))


# рисование кошек и клубков:
cat(100, 500, 40, grey, darkgrey)
cat(300, 350, 70, brown, darkbrown)
ooo(100, 350, 60, green, True)
ooo(450, 520, 30, blue, False)

pygame.display.update()
finished = False

while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # задание рандомного цвета неба в окне:
    color = list(np.random.choice(range(256), size=3))

    # рисование окон:
    for x in width / 6, 5 * width / 12, 2 * width / 3:
        window(x, 25, 100, tuple(color))

    pygame.display.update()

pygame.quit()