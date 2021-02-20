from sim.nanobot import Speed
from sim.nanobot import NanoBot
from physics.point import Point
from physics.matrix import UnusualMatrix

import os
import uuid

MATRICES_FILE_DIR = os.path.join(
    os.path.split(__file__)[0],
    "matrices"
)

if not os.path.isdir(MATRICES_FILE_DIR):
    os.mkdir(MATRICES_FILE_DIR)
    
class Planner:
    BOTS:[NanoBot]=[]
    PLANNING = False

    def __init__(self):
        self.FILEDATA = []
        self.CONDITION = lambda i, j:True

    def _plan(self):
        bot_create = 0
        for i in range(UnusualMatrix.SIZE):
            for j in range(UnusualMatrix.SIZE):
                if not bot_create == len(Planner.BOTS):
                    if self.CONDITION(i, j):
                        bot = Planner.BOTS[bot_create]
                        bot.speed = Speed()
                        bot.moveto(
                            Point(
                                x=(UnusualMatrix.START_X+(j*UnusualMatrix.SPACE)),
                                y=(UnusualMatrix.START_Y+(i*UnusualMatrix.SPACE)),
                            )
                        )
                        bot_create += 1
                    continue
            if bot_create == len(Planner.BOTS): break

    def plan(self):
        if not Planner.PLANNING:
            Planner.PLANNING = True
            if not self.FILEDATA:
                self._plan()
            else:
                bots = (bot for bot in Planner.BOTS)
                i = 0

                for bot in bots:
                    try:
                        bot.moveto(self.FILEDATA[i])
                        i += 1
                    except IndexError:
                        break

                for bot in bots:
                    bot.moveto(Point(-10, -10))

            Planner.PLANNING = False

    def fromfile(self, filename):
        with open(filename) as file:
            content = file.read().strip("\n").split("\n")
        for i, line in enumerate(content):
            for j, data in enumerate(line):
                if data=="*":
                    self.FILEDATA.append(
                        Point(
                            x=(UnusualMatrix.START_X+(j*UnusualMatrix.SPACE)),
                            y=(UnusualMatrix.START_Y+(i*UnusualMatrix.SPACE)),
                        )
                    )
        return self

    def fromcondition(self, condition):
        self.CONDITION = condition
        return self


import random

CONDITIONS = [
    lambda i, j: any([not i%8, not j%8]),
    lambda i, j: any([not i%10, not j%10]),
]

PLANS = [ Planner().fromcondition(condition) for condition in CONDITIONS ]
PLANS += [ Planner().fromfile(
        os.path.join(MATRICES_FILE_DIR, filename)
    ) for filename in os.listdir(MATRICES_FILE_DIR)
]
random.shuffle(PLANS)
