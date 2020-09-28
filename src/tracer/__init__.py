import os
import sys
import pygame
import random
from pygame import rect
from physics.matrix import UnusualMatrix

ROOT = os.path.split(__file__)[0]
FILENAME = None
MATRICES_FILE_DIR = os.path.join(ROOT, "../sim/matrices")

class Node:
    SIZE = 5
    SURFACE = None
    def __init__(self, x, y):
        self.black = False
        self.x = x
        self.y = y
        self._color = [random.randint(0, 150) for _ in range(3)]

    @property
    def color(self):
        return self._color if self.black else (255, 255, 255)

    def draw(self):
        if not Node.SURFACE: return
        pygame.draw.rect(
            Node.SURFACE,
            self.color,
            (self.x, self.y, Node.SIZE, Node.SIZE), 0
        )

    @property
    def rect(self):
        return rect.Rect(self.x, self.y, Node.SIZE, Node.SIZE)

if len(sys.argv) > 1:
    FILENAME = sys.argv[1]
    print("reading", FILENAME, "...")

    with open(FILENAME) as file:
        content = file.read().strip("\n").split("\n")

    nodes = []
    for i, line in enumerate(content):
        line_list = []

        for j, data in enumerate(line):
            node = Node(j*Node.SIZE, i*Node.SIZE)

            if data == "*":
                node.black = True

            line_list.append(node)
        nodes.append(line_list)

else:
    nodes = [
        [
            Node(j*Node.SIZE, i*Node.SIZE) for j in range(UnusualMatrix.SIZE) 
        ] for i in range(UnusualMatrix.SIZE)
    ]

SIZE = (nodes[-1][-1].x)+Node.SIZE
