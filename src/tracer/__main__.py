import os
import sys
import uuid
import pygame

pygame.init()

from . import SIZE
from . import Node
from . import nodes
from . import FILENAME
from . import MATRICES_FILE_DIR

from pygame import locals
from pygame.rect import Rect

window = pygame.display.set_mode((SIZE,)*2)
WIDTH = 2
RUNNING = True
HELDDOWN = False
ERASEMODE = False
CHANGESMADE = True

Node.SURFACE = window

while RUNNING:

    for event in pygame.event.get():
        if event.type == locals.QUIT:
            RUNNING = False
            break

        if event.type == locals.MOUSEBUTTONDOWN:
            HELDDOWN = True

        if event.type == locals.MOUSEBUTTONUP:
            HELDDOWN = False

        if event.type == locals.MOUSEMOTION:
            if HELDDOWN:
                CHANGESMADE = True
                rect = Rect(event.pos[0], event.pos[1], Node.SIZE*WIDTH, Node.SIZE*WIDTH)
                for row in nodes:
                    for node in row:
                        if node.rect.colliderect(rect):
                            if ERASEMODE:
                                node.black = False
                            else:
                                node.black = True

        if event.type == locals.KEYDOWN:

            if event.key == locals.K_e:
                ERASEMODE = not ERASEMODE
                print("switched eraze mode")

            if event.key == locals.K_s:
                if CHANGESMADE:

                    if FILENAME:
                        FILENAME = os.path.join(
                            os.getcwd(),
                            FILENAME
                        )
                    else:
                        FILENAME = os.path.join(MATRICES_FILE_DIR, str(uuid.uuid4()))
                    
                    data = ""

                    for row in nodes:
                        for node in row:
                            data +=  "*" if node.black else "-"
                        data += "\n"
                    data.strip("\n")

                    with open(os.path.join(MATRICES_FILE_DIR, FILENAME), "w") as file:
                        file.write(data)

                    print("print changes saved")

                    CHANGESMADE = False

    if not RUNNING: break

    window.fill((255,)*3)

    for row in nodes:
        for node in row:
            node.draw()

    pygame.display.flip()
pygame.quit()
sys.exit(0)