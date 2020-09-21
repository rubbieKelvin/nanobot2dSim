import random
from . import point

def iftrue(condition, funtion, *args, **kwargs):
	if condition: 
		return funtion(*args, **kwargs)

class UnusualMatrix:

	START_X = 10
	START_Y = 10
	SIZE	= 120
	SPACE	= 5
	
	def __init__(self):
		self._data = (
			(
				random.randint(0, 1) for _ in range(UnusualMatrix.SIZE)
			) for _ in range(UnusualMatrix.SIZE)
		)

	def pointMatrix(self):
		return (
			(
				point.Point(
					x=(UnusualMatrix.START_X+(j*UnusualMatrix.SPACE)),
					y=(UnusualMatrix.START_Y+(i*UnusualMatrix.SPACE)),
					z=x
				) for x, j in zip(y, range(UnusualMatrix.SIZE)) 
			) for y, i in zip(self._data, range(UnusualMatrix.SIZE))
		)
