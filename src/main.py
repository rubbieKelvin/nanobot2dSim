#!/usr/bin python3
import sys
import pygame
from pygame import init
from pygame.locals import QUIT, K_SPACE, KEYDOWN

from sim.matplanner import PLANS
from sim.matplanner import Planner

from sim.nanobot import NanoBot
from physics.point import Point
from sim.shape import NanoBotShape
from physics.matrix import UnusualMatrix

if __name__ == "__main__":
    init()

    index = -1

    SIZE = 620
    window = pygame.display.set_mode((SIZE,)*2)
    running = True

    NanoBotShape.SURFACE = window

    # create position matrix
    matrix = UnusualMatrix()

    # create nanobots
    nanobots = list()
    for y in matrix.pointMatrix():
        for x in y:
            if not x.visible:continue
            nanobots.append(NanoBot(x))

    # print(len(nanobots))

    shapes = [ NanoBotShape(bot) for bot in nanobots ]
    Planner.BOTS = nanobots
    
    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    index += 1
                    index %= len(PLANS)
                    planner = PLANS[index]
                    planner.plan()
            
        if not running: break

        window.fill([255]*3)

        for shape in shapes:
            shape.draw()

        pygame.display.flip()
    
    pygame.quit()
    sys.exit(0)
    
sys.exit(1)