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

    def _plan(self):
        bot_create = 0
        for i in range(UnusualMatrix.SIZE):
            for j in range(UnusualMatrix.SIZE):
                if not bot_create == len(Planner.BOTS):
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
                for i, bot in enumerate(Planner.BOTS):
                    try:
                        bot.moveto(self.FILEDATA[i])
                    except IndexError:
                        break

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

class Mul3Planner(Planner):
    def _plan(self):
        bot_create = 0
        for i in range(UnusualMatrix.SIZE):
            for j in range(UnusualMatrix.SIZE):
                if not bot_create == len(Planner.BOTS):
                    if not (j*i)%3:
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

class Mul5Planner(Planner):
    def _plan(self):
        bot_create = 0
        for i in range(UnusualMatrix.SIZE):
            for j in range(UnusualMatrix.SIZE):
                if not bot_create == len(Planner.BOTS):
                    if not (j*i)%5:
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

class Mul8Planner(Planner):
    def _plan(self):
        bot_create = 0
        for i in range(UnusualMatrix.SIZE):
            for j in range(UnusualMatrix.SIZE):
                if not bot_create == len(Planner.BOTS):
                    if not (j*i)%8:
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

import random
PLANS = [ Planner(), Mul3Planner(), Mul5Planner(), Mul8Planner() ]
PLANS += [ Planner().fromfile(
        os.path.join(MATRICES_FILE_DIR, filename)
    ) for filename in os.listdir(MATRICES_FILE_DIR)
]
random.shuffle(PLANS)
