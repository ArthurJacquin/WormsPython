import pygame
from Worms.Vector2 import *
from Worms.Physics import *

class Grenade():
	"""This class represents the grenade weapon"""
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.vel = 1

	def draw(self, window):
		"""Draw bullet"""
		pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

	def drawCurve(self, window):
		"""Draw curve"""
		pygame.draw.lines(window, self.color, self.start, self.end, 3)

	def grenadeShot(self):
		vzero = (0,0)
		shot = -1/2*(9.1/vzero)
		speedVector = Physics.CalculateSpeedVector(self.vel, 45)
		newPos = Physics.CalculateNexPosition(Vector2(self.x, self.y), speedVector, 0.1, Vector2(0, 0))
		self.x = newPos.x
		self.y = newPos.y

