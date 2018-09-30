import sys, pygame
from pygame.locals import *
from random import randrange

up = lambda x: (x[0] - 1, x[1])  # 本代码中 ,,Y从左往右递增，X从上往下递增 ,, 最左上方可见像素的坐标是（0，0）
down = lambda x: (x[0] + 1, x[1])
left = lambda x: (x[0], x[1] - 1)
right = lambda x: (x[0], x[1] + 1)
dire = [up, left, down, right]
move = lambda x, y: [y(x[0])] + x[:-1]
grow = lambda x, y: [y(x[0])] + x
FPSCLOCK = pygame.time.Clock()
pygame.init()  # 忽视此错误,可能仅是显示错误
pygame.display.set_mode((800, 600))
pygame.mouse.set_visible(0)
screen = pygame.display.get_surface()
screen.fill((0, 0, 0))
times = 0.0
s = [(5, 5), (5, 6), (5, 7)] # 横着出现,
food = randrange(0, 30), randrange(0, 40)
d = up
while True:
    time_passed = FPSCLOCK.tick(30)
    if times >= 150:
        times = 0.0
        s = move(s, d)
    else:
        times += time_passed
    for event in pygame.event.get():
        if event.type == KEYDOWN and d != down and event.key == K_UP:  #
            d = up
            s = move(s, d)
        if event.type == KEYDOWN and d != right and event.key == K_LEFT:
            d = left
            s = move(s, d)
        if event.type == KEYDOWN and d != left and event.key == K_RIGHT:
            d = right
            s = move(s, d)
        if event.type == KEYDOWN and d != up and event.key == K_DOWN:
            d = down
            s = move(s, d)
    if s[0] == food:
        s = grow(s, d)
        food = randrange(0, 30), randrange(0, 40)
    if s[0] in s[1:] or s[0][0] < 0 or s[0][0] >= 30 or s[0][1] < 0 or s[0][1] >= 40:  # 判断出界
        print("yao zhu la")
        break
    screen.fill((0, 0, 0))
    for r, c in s:
        pygame.draw.rect(screen, (255, 0, 0), (c * 20, r * 20, 20, 20))
        pygame.draw.rect(screen, (0, 255, 0), (food[1] * 20, food[0] * 20, 20, 20))
        pygame.display.update()
