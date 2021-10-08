import pygame
import random
from pygame.draw import *
from random import randint
pygame.init()

FPS = 5
screen = pygame.display.set_mode((1200, 900))

''' Задание цветов '''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
objects = []

def new_ball():
    '''
    Создаёт новый шарик как объект.
    x, y - координаты центра шарика.
    r - радиус шарика.
    color - цвет шарика.
    dx - скорость шарика по оси х.
    dy - скорость шарика по оси у.
    '''
    global r, x, y, dx, dy
    r = randint(10, 100)
    x = randint(100, 1100)
    y = randint(100, 900)
    dx = randint(0, 10)
    dy = randint(0, 10)
    color = COLORS[randint(0, 5)]
    ball = {'color': color, 'r': r, 'p': {'x': x, 'y': y}, 'v': {'x': dx, 'y': dy}}
    balls.append(ball)

def new_object():
    '''
    Создаёт новый объект.
    x, y - координаты левого верхнего угла объекта.
    l - характерный линейный размер объекта.
    color - цвет объекта.
    '''
    global l, x, y, dx, dy
    l = randint(10, 100)
    x = randint(100, 1100)
    y = randint(100, 900)
    dx = randint(0, 10)
    dy = randint(0, 10)
    color = COLORS[randint(0, 5)]
    object = {'color': color, 'l': l, 'p': {'x': x, 'y': y}, 'v': {'x': dx, 'y': dy}}
    objects.append(object)

def draw_ball(x, y, r, color):
    '''
    Рисует шарик.
    x, y - координаты центра шарика.
    r - радиус шарика.
    color - цвет шарика.
    '''
    circle(screen, color, (x, y), r)

def draw_object(x, y, l, color):
    '''
    Рисует объект.
    x, y - координаты левого верхнего угла объекта.
    l - характерный линейный размер объекта.
    color - цвет объекта.
    '''
    rect(screen, color, (x, y, l, l))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

dt1 = 10 # таймер для движения шариков
dt2 = 20 # таймер для движения объектов
S = 0 # сумма очков
pos = [0, 0]

# Создание исходных шариков
for i in range(10):
    new_ball()

# Создание исходных объектов
for i in range(5):
    new_object()

# Диалог с пользователем:
print("Введите Ваше имя: ")
name = input()


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print('Click!')

    for ball in balls:
        if ball['p']['x'] >= 1100 or ball['p']['x'] <= 50: # Обработка отражений от левой и правой стенок
            ball['v']['x'] *= - 1
        if ball['p']['y'] >= 450 or ball['p']['y'] <= 50: # Обработка отражений от верхней и нижней стенок
            ball['v']['y'] *= - 1
        # Перемещение шарика:
        ball['p']['x'] += ball['v']['x'] * dt1
        ball['p']['y'] += ball['v']['y'] * dt1
        # Рисоване шарика в новой точке пространства:
        draw_ball(ball['p']['x'], ball['p']['y'], ball['r'], ball['color'])

        # Отработка попадания/промаха пользователя:
        if (ball['p']['x'] - pos[0]) ** 2 + (ball['p']['y'] - pos[1]) ** 2 <= ball['r'] ** 2:
            S += 1
            balls.remove(ball)
            new_ball()

    for object in objects:
        if object['p']['x'] >= 1100 or object['p']['x'] <= 50: # Обработка отражений от левой и правой стенок
            object['v']['x'] *= - 1
        if object['p']['y'] >= 450 or object['p']['y'] <= 50: # Обработка отражений от верхней и нижней стенок
            object['v']['y'] *= - 1
        # Перемещение объекта:
        object['p']['x'] += object['v']['x'] * dt2 * random.random()
        object['p']['y'] += object['v']['y'] * dt2 * random.random()
        # Рисоване объекта в новой точке пространства:
        draw_object(object['p']['x'], object['p']['y'], object['l'], object['color'])

        # Отработка попадания/промаха пользователя:
        if (object['p']['x'] - pos[0]) ** 2 + (object['p']['y'] - pos[1]) ** 2 <= object['l'] ** 2:
            S += 5
            objects.remove(object)
            new_object()

    print("Сумма очков: ", S)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()


# Добавление игрока в таблицу рекордов:
l = []
dict = {}
f = open('Таблица рекордов.txt', 'r+')

# Считывание результатов всех игроков из файла:
while True:
    line = f.readline()
    if not line:
        break
    l.append(line.strip())

for x in l:
    player = x.split(' : ')
    dict[player[0]] = int(player[1])

# Добавление текущего игрока в рейтинг:
dict[name] = S

# Сортировка игроков по убыванию числа очков:
d = {k: dict[k] for k in sorted(dict, key=dict.get, reverse=True)}

f.close()

# Обновление рейтинга в файле:
with open('Таблица рекордов.txt', "w") as file:
    for player in d:
        file.write(player + ' : ' + str(d[player]) + '\n')