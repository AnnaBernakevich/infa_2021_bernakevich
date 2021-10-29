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


class Ball():
    def __init__(self, screen: pygame.Surface, x=60, y=450):
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

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(tank)
        self.image = pygame.image.load('tank.png')
        self.w = self.image.get_width() // 7
        self.h = self.image.get_height() // 7
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
        self.direction = True
        self.rect.left = x
        self.rect.top = y
        self.lives = 5

class Gun():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = x
        self.y = y
        self.l = 3
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, x, y):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        new_ball.x = x
        new_ball.y = y
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
             (self.x + math.sin(self.an) * self.l, self.y - math.cos(self.an) * self.l),
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

    def move(self, dx, dy):
            self.x += dx
            self.y += dy
            if self.x <= 0:
                self.x = 0
            if self.x >= WIDTH:
                self.x = WIDTH
            if self.y <= 0:
                self.y = 0
            if self.y >= HEIGHT:
                self.y = HEIGHT

class Target():
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

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bomb.png')
        self.w = self.image.get_width() // 7
        self.h = self.image.get_height() // 7
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.vy = random.randrange(1, 10)

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.vy = random.randrange(5, 10)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tank = pygame.sprite.Group()
bombs = pygame.sprite.Group()

Font = pygame.font.SysFont("arial", 15)
score = 0
bullet = 0
balls = []
clock = pygame.time.Clock()
gun_1 = Gun(screen, 110, 480)
tank_1 = Tank(10, 440)
target_1 = Target()
target_2 = Target()

for i in range(3):
    b = Bomb()
    bombs.add(b)

finished = False

while not finished:
    screen.fill(WHITE)
    gun_1.draw()
    target_1.draw()
    target_2.draw()
    dx = 0
    dy = 0
    for b in balls:
        b.draw()

    tank.draw(screen)
    bombs.draw(screen)
    tank.update()
    bombs.update()

    scoring = Font.render('Score: ' + str(score), 1, BLUE)
    screen.blit(scoring, (350, 10))
    living = Font.render('Lives: ' + str(tank_1.lives), 1, BLUE)
    screen.blit(living, (350, 40))

    pygame.display.update()

    hits = pygame.sprite.spritecollide(tank_1, bombs, True) # проверка, не попал ли снаряд в танк
    if hits:
        tank_1.lives -= 1

    if tank_1.lives == 0:
        finished = True

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun_1.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun_1.fire2_end(event, gun_1.x, gun_1.y)
        elif event.type == pygame.MOUSEMOTION:
            gun_1.targetting(event)
        elif event.type == pygame.KEYDOWN: # обработка движения танка с пушкой
            if event.key == pygame.K_LEFT:
                dx = -10
                if tank_1.direction: # обрабатывает поворот танка
                    tank_1.image = pygame.transform.flip(tank_1.image, True, False)
                    tank_1.direction = False
            elif event.key == pygame.K_RIGHT:
                dx = 10
                if not tank_1.direction: # обрабатывает поворот танка
                    tank_1.image = pygame.transform.flip(tank_1.image, True, False)
                    tank_1.direction = True
            elif event.key == pygame.K_DOWN:
                dy = 10
            elif event.key == pygame.K_UP:
                dy = -10

    gun_1.move(dx, dy)
    tank_1.rect.x += dx
    tank_1.rect.y += dy
    for b in balls:
        b.move()
        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1.new_target()
            score += 10
        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
            score += 15

    target_1.move()
    target_2.move()
    gun_1.power_up()

pygame.quit()
