import pygame
from Worms.Physics import *

class Grenade():
	"""This class represents the grenade weapon"""
	def __init__(self, x, y, radius, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = (0, 0, 255)
		self.vel = 0
		self.facing = facing
		self.mass = 5
		self.rebonds = 0

	def draw(self, window):
		"""Draw bullet"""
		pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

	def drawCurve(self, window):
		"""Draw curve"""
		pygame.draw.lines(window, self.color, self.start, self.end, 3)

	# Setup the rocket object for a shoot
	def setupForShoot(self, player, facing):
		self.x = round(player.x + player.width // 2)
		self.y = round(player.y + player.height // 2)
		self.radius = 6
		self.facing = facing