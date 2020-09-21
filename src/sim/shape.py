import pygame
import random
from . import nanobot

class NanoBotShape:
	SURFACE = None

	def __init__(self, bot:nanobot.NanoBot):
		self.bot = bot
		self.color = (0, 0, 0)

	def draw(self):
		self.bot.update()

		pygame.draw.circle(
			self.surface, 
			self.color,
			(
				int(self.bot.point.x),
				int(self.bot.point.y),
			), 
			2, 0
		)

	@property
	def surface(self):
		if NanoBotShape.SURFACE:
			return NanoBotShape.SURFACE
		raise TypeError("Shape has not been given surface")