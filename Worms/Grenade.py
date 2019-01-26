import pygame 
import Worms.Vector2 import Vector2
import Worms.Rocket import Rocket


class Grenade(Rocket):
	"""This class represents the grenade weapon herited from rocket"""
	def __init__(self, x, y, radius, color):
		Rocket.__init__(self, x, y, radius, color)

	def draw(self, window):
		pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)
