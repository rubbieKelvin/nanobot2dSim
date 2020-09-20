import random
from . import point

def iftrue(condition, funtion, *args, **kwargs):
	if condition: 
		return funtion(*args, **kwargs)

class UnusualMatrix:

	START_X = 100
	START_Y = 100
	SIZE	= 60
	SPACE	= 7
	
	def __init__(self):
		self._data = (
			(
				random.choice(( *(0,)*3, 1 )) for _ in range(UnusualMatrix.SIZE)
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
