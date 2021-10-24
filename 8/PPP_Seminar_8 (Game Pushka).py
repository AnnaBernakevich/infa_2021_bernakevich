import math
from random import choice
import pygame
import random
from pygame.draw import *


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g = 0.5 # ускорение свободного падения
k = 0.7 # коэффициент затухания скорости шарика при ударе о стенку


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y += self.vy
        self.vy += g

        if self.x > (WIDTH - 5):   # Обработка отражений от левой и правой стенок
            self.vx *= - k
            self.vy *= k
            self.x = WIDTH - 5
        if self.x < 5:
            self.vx *= - k
            self.vy *= k
            self.x = 5
        if self.y > (HEIGHT - 5):  # Обработка отражений от верхней и нижней стенок
            self.vx *= k
            self.vy *= - k
            self.y = HEIGHT - 5
        if  self.y < 5:
            self.vx *= k
            self.vy *= - k
            self.y = 5

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        d = (self.x - obj.x)**2 + (self.y - obj.y)**2
        if d <= (self.r + obj.r)**2:
            return True
        return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = 50
        self.y = 450
        self.l = 3
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - math.sin(self.an) * self.l, self.y + math.cos(self.an) * self.l),
             (self.x + math.sin(self.an) * self.l, self.y - math.cos(self.an)*self.l),
             (self.x + math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power,
              self.y - math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power),
             (self.x - math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power,
              self.y + math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power)]
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.vx = random.randint(5, 20)
        self.vy = random.randint(5, 20)
        self.r = random.randint(2, 50)
        self.color = BLACK
        self.points = 0
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(2, 50)
        self.color = BLACK
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += random.randint(-5, 5)/10
        self.vy += random.randint(-5, 5)/10

        if self.x > (WIDTH - 5):   # Обработка отражений от левой и правой стенок
            self.vx *= - k
            self.vy *= k
            self.x = WIDTH - 5
        if self.x < 5:
            self.vx *= - k
            self.vy *= k
            self.x = 5
        if self.y > (HEIGHT - 50):  # Обработка отражений от верхней и нижней стенок
            self.vx *= k
            self.vy *= - k
            self.y = HEIGHT - 50
        if  self.y < 5:
            self.vx *= k
            self.vy *= - k
            self.y = 5



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bullet = 0
balls = []
clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target()
target_2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1.new_target()
        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
    target_1.move()
    target_2.move()
    gun.power_up()

pygame.quit()
