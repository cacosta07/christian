from re import X
import pygame
import numpy as np
import sys

global brightness
global resolution
global zoom

global depthAdd

brightness = 8
resolution = 8
zoom = 1

# Initialize pygame
pygame.init()

# Set up display
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Window")
screen.fill("#000000")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up font
font = pygame.font.Font(None, 74)
text = font.render("Default Text", True, BLACK)
text_rect = text.get_rect(center=(width // 2, height // 2))

# Game loop
clock = pygame.time.Clock()
running = True

def drawDepth():
    xoffset = 0
    yoffset = 0
    for offsetCount in range(4):
        if offsetCount == 1:
            xoffset += .5
        if offsetCount == 2:
            yoffset += .5
        if offsetCount == 3:
            xoffset -= .5

            for screenx in range(round(width / resolution)):
                x = ((screenx * resolution) / zoom) + xoffset
                if screenx % ((resolution)**4):
                    pygame.display.update()
                for screeny in range(round(height / resolution)):
                    y = ((screeny * resolution) / zoom) + yoffset

                    try:
                        ################
                        ################

                        depth = x/y

                        ################
                        ################
                        depthAdd += depth
                        if np.isnan(depthAdd):
                            depthAdd = (np.sin(x/4)*99999999) * (np.cos(y/4)*99999999)
                    except:
                        depthAdd = (np.sin(x/4)*99999999) * (np.cos(y/4)*99999999)

                    depthAdd /= 4

                    depthOutput = [np.clip(depthAdd * brightness, 0, 255), np.clip(depthAdd * brightness, 0, 255), np.clip(depthAdd * brightness, 0, 255)]

                    pygame.draw.rect(screen, depthOutput, pygame.Rect(screenx * resolution, screeny * resolution, round(resolution * .8), round(resolution * .8)))

drawDepth()

while running:
    # Handle events

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        brightness *= 2
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        brightness *= .5
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and resolution > 1:
        resolution -= 1
        screen.fill("#000000")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        resolution += 1
        screen.fill("#000000")
    if keys[pygame.K_PLUS] or keys[pygame.K_e]:
        zoom *= 2
    if keys[pygame.K_MINUS] or keys[pygame.K_q]:
        zoom *= .5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if (brightness <= 0):
                brightness = .001
            print(brightness)

            drawDepth()
    
    if any(keys):
        drawDepth()

    print(clock.get_fps())

    # Control frame rate
    clock.tick(30)


# Quit
pygame.quit()
sys.exit()
