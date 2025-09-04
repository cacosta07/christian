import pygame
import random as rand
global font
import numpy as np
import sys

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mines")
screen.fill("#000000")

font = pygame.font.Font(None, 30)


def textRender(text, location, color=(255, 255, 255)):
  screen.blit(font.render(text, True, color), location)


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mines = []
unearthed = []
flags = []

clock = pygame.time.Clock()
running = True
mines = [[0 for _ in range(10)] for _ in range(10)]
unearthed = [[0 for _ in range(10)] for _ in range(10)]
flags = [[0 for _ in range(10)] for _ in range(10)]


def placeMines():
  for y in range(10):
    for x in range(10):
      mines[x][y] = 0
      unearthed[x][y] = 0
      flags[x][y] = 0

      try:
        if rand.randint(0, 5) == 0:
          mines[x][y] = "x"
        else:
          mines[x][y] = 0
      except:
        pass
  for y in range(10):
    for x in range(10):
      for i in range(-1, 1 + 1):
        try:
          if mines[x + i][y + 1] == "x":
            mines[x][y] += 1
        except:
          pass
      for i in range(-1, 1 + 1):
        try:
          if mines[x + i][y] == "x" and i != 0:
            mines[x][y] += 1
        except:
          pass
      for i in range(-1, 1 + 1):
        try:
          if mines[x + i][y - 1] == "x":
            mines[x][y] += 1
        except:
          pass


def draw():
  for y in range(10):
    for x in range(10):

      color = WHITE
      if mines[x][y] == "x":
        color = BLUE
      if mines[x][y] == 1:
        color = GREEN
      if mines[x][y] == 2:
        color = YELLOW
      if mines[x][y] == 3:
        color = ORANGE
      if mines[x][y] == 4:
        color = RED
      if mines[x][y] == 5:
        color = PURPLE
      if mines[x][y] == 6:
        color = PINK
      if mines[x][y] == 7:
        color = CYAN
      if mines[x][y] == 8:
        color = BLACK
      if pygame.mouse.get_pos()[0] > 5 + x * 60 and pygame.mouse.get_pos(
      )[0] < 62 + x * 60 and pygame.mouse.get_pos(
      )[1] > 5 + y * 60 and pygame.mouse.get_pos()[1] < 62 + y * 60:
        pygame.draw.rect(screen, RED, pygame.Rect(5 + x * 60, 5 + y * 60, 58,
                                                  5))
        pygame.draw.rect(screen, RED, pygame.Rect(5 + x * 60, 5 + y * 60, 5,
                                                  58))
        pygame.draw.rect(screen, RED,
                         pygame.Rect(5 + x * 60, 58 + y * 60, 58, 5))
        pygame.draw.rect(screen, RED,
                         pygame.Rect(58 + x * 60, 5 + y * 60, 5, 58))

      pygame.draw.rect(screen, color,
                       pygame.Rect(5 + x * 60, 5 + y * 60, 58, 58))
      if mines[x][y] != 0 and mines[x][y] != "x":
        textRender(str(mines[x][y]), (28 + x * 60, 25 + y * 60), BLACK)
      if mines[x][y] == "x":
        textRender("X", (27 + x * 60, 26 + y * 60), WHITE)
      if unearthed[x][y] == 0:
        pygame.draw.rect(screen, (128, 128, 128),
                         pygame.Rect(5 + x * 60, 5 + y * 60, 58, 58))
        if pygame.mouse.get_pos()[0] > 5 + x * 60 and pygame.mouse.get_pos(
        )[0] < 62 + x * 60 and pygame.mouse.get_pos(
        )[1] > 5 + y * 60 and pygame.mouse.get_pos()[1] < 62 + y * 60:
          pygame.draw.rect(screen, RED,
                           pygame.Rect(5 + x * 60, 5 + y * 60, 58, 5))
          pygame.draw.rect(screen, RED,
                           pygame.Rect(5 + x * 60, 5 + y * 60, 5, 58))
          pygame.draw.rect(screen, RED,
                           pygame.Rect(5 + x * 60, 58 + y * 60, 58, 5))
          pygame.draw.rect(screen, RED,
                           pygame.Rect(58 + x * 60, 5 + y * 60, 5, 58))
      if flags[x][y] == 1:
        pygame.draw.circle(screen, (0, 25, 0), (34 + x * 60, 34 + y * 60),23)
        pygame.draw.circle(screen, (0, 180, 0), (34 + x * 60, 34 + y * 60),20)
        pygame.draw.circle(screen, (0, 130, 0), (34 + x * 60, 34 + y * 60),17)
        pygame.draw.circle(screen, (0, 180, 0), (34 + x * 60, 34 + y * 60),14)
        pygame.draw.circle(screen, (0, 130, 0), (34 + x * 60, 34 + y * 60),11)
        pygame.draw.circle(screen, (0, 180, 0), (34 + x * 60, 34 + y * 60),8)
        pygame.draw.circle(screen, (0, 130, 0), (34 + x * 60, 34 + y * 60),5)
        pygame.draw.circle(screen, (0, 180, 0), (34 + x * 60, 34 + y * 60),2)
  pygame.display.flip()


def click():
  for y in range(10):
    for x in range(10):
      if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] > 5 + x * 60 and pygame.mouse.get_pos(
        )[0] < 62 + x * 60 and pygame.mouse.get_pos(
        )[1] > 5 + y * 60 and pygame.mouse.get_pos()[1] < 62 + y * 60:
          print(x, y, ":", mines[x][y])
          if flags[x][y] == 0:
            unearthed[x][y] = 1
            if mines[x][y] == 0:
              unearth(x, y)
          if mines[x][y] == "x" and flags[x][y] == 0:
            print("You lose")
            for y in range(10):
              for x in range(10):
                unearthed[x][y] = 1


def flag():
  for y in range(10):
    for x in range(10):
      if pygame.mouse.get_pressed()[2]:
        if pygame.mouse.get_pos()[0] > 5 + x * 60 and pygame.mouse.get_pos(
        )[0] < 62 + x * 60 and pygame.mouse.get_pos(
        )[1] > 5 + y * 60 and pygame.mouse.get_pos()[1] < 62 + y * 60:
          if flags[x][y] == 0 and unearthed[x][y] == 0:
            flags[x][y] = 1
          else:
            flags[x][y] = 0
          print(x, y, ":", flags[x][y])


def unearth(x, y):
  for i in range(-1, 1 + 1):
    try:
      if unearthed[x + i][y + 1] == 0 and flags[x + i][y + 1] == 0:
        unearthed[x + i][y + 1] = 1
        if mines[x + i][y + 1] == 0:
          unearth(x + i, y + 1)
    except:
      pass
  for i in range(-1, 1 + 1):
    try:
      if unearthed[x + i][y] == 0 and flags[x + i][y] == 0:
        unearthed[x + i][y] = 1
        if mines[x + i][y] == 0:
          unearth(x + i, y)
    except:
      pass
  for i in range(-1, 1 + 1):
    try:
      if unearthed[x + i][y - 1] == 0 and flags[x + i][y - 1] == 0:
        unearthed[x + i][y - 1] = 1
        if mines[x + i][y - 1] == 0:
          unearth(x + i, y - 1)
    except:
      pass


placeMines()

while running:

  draw()
  click()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      placeMines()
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
      flag()

  clock.tick(30)

pygame.quit()
sys.exit()
