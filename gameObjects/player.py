import pyglet
from pyglet.window import key
from gameObjects import resources, entity

class Player(entity.Entity):
	def __init__(self, vis = False, scale = 1, *args, **kwargs):
		super(Player, self).__init__(img = resources.playerImageRight, *args, **kwargs)
		self.visible = vis
		self.scale = scale
		
		self.lives = 3
		self.maxLives = self.lives
		
		self.score = 0
		self.scoreLabel = pyglet.text.Label("Score: 0", font_name = "Times New Roman", font_size = 20,
						    x = 750, y = 570,
						    anchor_x = "center", anchor_y = "center")
	
		self.keyHandler = key.KeyStateHandler()
		self.eventHandlers = [self, self.keyHandler]
		
		self.startFalling()
	# end init
	
	def update(self, dt):
		super(Player, self).update(dt)
		
		if self.keyHandler[key.LEFT]:
			self.dx = -self.moveSpeed
			self.moveDir = -1
			self.image = resources.playerImageLeft
		# end if
		if self.keyHandler[key.RIGHT]:
			self.dx = self.moveSpeed
			self.moveDir = 1
			self.image = resources.playerImageRight
		# end if
		if self.keyHandler[key.SPACE] and not self.isFalling():
			self.dy = self.jumpingSpeed
			self.startFalling()
		# end if
		if self.keyHandler[key.SPACE] and self.isFalling():
			if self.dy <= 30:
				self.dy = self.flyUpSpeed
			# end if
		# end if
		if not(self.keyHandler[key.LEFT] or self.keyHandler[key.RIGHT]):
			if self.moveDir != 0:
				self.dx -= self.moveDir * self.dragFactor
			# end if
			if self.moveDir == 1:
				if self.dx < 0:
					self.dx = 0
					self.moveDir = 0
				# end if
			# end if
			elif self.moveDir == -1:
				if self.dx > 0:
					self.dx = 0
					self.moveDir = 0
				# end if
			# end if
		# end if

		self.checkBounds(dt)
		
		self.checkFalling()
	# end update
	
	def checkBounds(self, dt):
		minX = -self.image.width / 2
		maxX = 800 + (self.image.width / 2)
		minY = 24
		maxY = 600
	
		if self.x > maxX:
			self.x = minX
		# end if
		if self.x < minX:
			self.x = maxX
		# end if
		if self.imgBottom < minY:
			self.kill()
		# end if
		nextPosUp = self.y + self.dy * dt
		nextPosUp += self.image.height / 2
		if nextPosUp >= maxY:
			self.dy = 0
			self.startFalling()
		# end if
	# end checkBounds
	
	def kill(self):
		super(Player, self).kill()
		
		self.decLives()
	# end kill
	
	def checkLives(self):
		return self.lives
	# end checkLives
	
	def decLives(self):
		if self.lives != 0:
			self.lives -= 1
	# end decLives
	
	def resetLives(self):
		self.lives = self.maxLives
	# end resetLives
	
	def incScore(self):
		self.score += 1
	# end incScore
	
	def resetScore(self):
		self.score = 0
	# end resetScore
	
	def getScore(self):
		return self.score
	# end getScore
	
	def drawScore(self):
		self.scoreLabel.text = f"Score: {self.score}"
		self.scoreLabel.draw()
	# end drawScore
# end Player
