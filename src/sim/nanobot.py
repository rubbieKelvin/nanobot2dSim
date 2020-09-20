import math
import random
from physics.point import Point

class Speed:
	def __init__(self):
		self.vary = random.randint(0, 1)
		self._speed = random.randint(1, 10)/10

	@property
	def value(self):
		if self.vary:
			return random.randint(1, 10)/10
		return self._speed
		
def inrange(cur, pnt, rad):
	"""if cur is in (rad-pnt) to (rad.pnt)"""
	return (cur > pnt-rad) and (cur < pnt+rad)

class NanoBot(object):
	def __init__(self, point:Point):
		super(NanoBot, self).__init__()
		self.dest = point
		self.point = Point(0, 0, point.visible)

		self.angle = self.point.angle(self.dest)
		self.speed = Speed()

	def moveto(self, point:Point):
		self.dest = point
		self.angle = self.point.angle(self.dest)
		# self.speed = Speed()

	def update(self):
		# thee goal is to get to the the point from dest
		if not inrange(self.point.x, self.dest.x, self.speed.value/2):
			if self.point.x < self.dest.x: self.point.x += (20*math.radians(math.sin(self.angle))) + self.speed.value
			else: self.point.x -= (20*math.radians(math.sin(self.angle))) + self.speed.value

		if not inrange(self.point.y, self.dest.y, self.speed.value/2):
			if self.point.y < self.dest.y: self.point.y += (20*math.radians(math.cos(self.angle))) + self.speed.value
			else: self.point.y -= (20*math.radians(math.cos(self.angle))) + self.speed.value