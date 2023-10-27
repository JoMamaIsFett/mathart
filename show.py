import numpy as np
import pygame
from pygame import gfxdraw
import sys
import os

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

zoom = 450
xoffset = 0
yoffset = 0
width = screen.get_width()
height = screen.get_height()


punkte = np.load('points.npy')

werte = [item for tupel in punkte for item in tupel]
maxwert = max(werte)
minwert = min(werte)
step = 255 / (maxwert - minwert)


def render():
    screen.fill((245, 255, 252))
    for i in punkte:
        x, y = i
        xpos = int(width / 2 + zoom * x + xoffset)
        ypos = int(height / 2 + zoom * y + yoffset)
        if 0 < xpos < width and 0 < ypos < height:
            try:
                gfxdraw.pixel(screen, xpos, ypos, (int((x - minwert) * step), int((y - minwert) * step), int((y + x - 2 * minwert) * (step / 4))))
            except:
                gfxdraw.pixel(screen, xpos, ypos, (0, 0, 0))


def ausgabe():
    os.system('cls' if os.name == 'nt' else 'clear')
    if zoom < 10:
        print("Zoom:", zoom)
    else:
        print("Zoom:", int(zoom))
    print("x offset:", xoffset)
    print("y offset:", yoffset)


ausgabe()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mausrad nach oben
                zoom *= 1.1
            elif event.button == 5:  # Mausrad nach unten
                if zoom > 0:
                    zoom *= 0.9
            ausgabe()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yoffset += 25
            ausgabe()
        elif keys[pygame.K_s]:
            yoffset -= 25
            ausgabe()
        elif keys[pygame.K_a]:
            xoffset += 25
            ausgabe()
        elif keys[pygame.K_d]:
            xoffset -= 25
            ausgabe()


    render()
    pygame.display.update()
