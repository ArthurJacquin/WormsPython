import pygame
from Worms.Physics import *

class Grenade():
	"""This class represents the grenade weapon"""
	def __init__(self, x, y, radius, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = (0, 0, 255)
		self.vel = 10
		self.facing = facing

	def draw(self, window):
		"""Draw bullet"""
		pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

	def drawCurve(self, window):
		"""Draw curve"""
		pygame.draw.lines(window, self.color, self.start, self.end, 3)

	def grenadeShot(self):
		speedVector = Physics.CalculateSpeedVector(self.vel, 45,self.facing)
		newPos = Physics.CalculateNexPosition(pygame.math.Vector2(self.x, self.y), speedVector, 0.1, pygame.math.Vector2(0, 0))
		self.x = newPos.x
		self.y = newPos.y

