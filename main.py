import os
import sys

import pygame as pyg


WINDOW_SIZE = (1920, 1080)
BG_Color = (0, 0, 0)

pyg.init()

screen = pyg.display.set_mode(WINDOW_SIZE)

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT: sys.exit()

    screen.fill(BG_Color)
    pyg.display.flip()