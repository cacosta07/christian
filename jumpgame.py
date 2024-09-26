import pygame
import random
import math
import numpy as np
import pygame.examples

def init_screen_and_clock():
    global screen, display, clock, WINDOW_SIZE
    pygame.init()
    WINDOW_SIZE = (600, 900)
    pygame.display.set_caption('Game')
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    clock = pygame.time.Clock()


def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(
        fonts[1],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))
    
cursor_list = []

    
init_screen_and_clock()
# This create different font size in one line
fonts = create_fonts([24, 16, 14, 8])
pygame.mouse.set_visible(False)
score = 0

class Object:
    def __init__(self):
        self.radius = 5
        self.pos = pygame.mouse.get_pos()
    
    def draw(self):
        pygame.draw.circle(screen, "#cccccc", object.pos, object.radius)

    def change(self):
        self.radius -= 0.1
        

loop = 1
ballpos = [40,40]
while loop:
    screen.fill(0)
    position = 0,0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        elif event.type == pygame.K_DOWN:
            if pygame.KEYDOWN == pygame.K_SPACE:
                print("Space")

    pygame.draw.circle(screen, "#dd00dd", ballpos, 20)
    cursor_list.append(Object())
    for object in cursor_list[:]:
        object.draw()
        object.change()
    
    pygame.display.flip()
    clock.tick(480)
    

pygame.quit()
print("Quitting")