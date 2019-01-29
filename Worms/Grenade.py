import pygame 
import Worms.Vector2
import Worms.Rocket


class Grenade(pygame.sprite.Sprite):
	"""This class represents the grenade weapon"""
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color

	def draw(self, window):
		"""Draw bullet"""
		pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

	def drawCurve(self, window):
		"""Draw curve"""
		pygame.draw.lines(window, self.color, self.start, self.end, 3)
