import math

class Point:
	def __init__(self, x, y, z=True):
		self.x=x
		self.y=y
		self.visible=z

	def __repr__(self):
		return f"<{self.x}, {self.y}>"

	def angle(self, point):
		dy = point.y - self.y
		dx = point.x - self.x
		return math.atan2(dy, dx)