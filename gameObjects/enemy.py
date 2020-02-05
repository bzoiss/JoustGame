import pyglet, random
from gameObjects import resources, entity

class Enemy(entity.Entity):
	def __init__(self, *args, **kwargs):
		super(Enemy, self).__init__(img = resources.enemyImageRight, *args, **kwargs)
		
		self.moveSpeedOffset = 60 - random.randint(0, 60)
		self.moveSpeed += self.moveSpeedOffset
		
		self.falling = False	

		self.maxChance = 25
		self.jumpChance = .2
		self.flyChance = .2
		
		# randomly pick movement direction
		self.moveDir = random.randint(-1, 1)
		if self.moveDir == 0:
			self.moveDir = -1
			self.image = resources.enemyImageLeft
		else:
			self.moveDir = 1
		# end if
		
		self.startFalling()
	# end __init__
	
	def update(self, dt):
		super(Enemy, self).update(dt)
		
		# enemy movement
		self.dx = self.moveSpeed * self.moveDir
		
		jumpNum = random.randint(0, self.maxChance)
		if not self.falling:
			if jumpNum / self.maxChance == self.jumpChance and self.dy == 0:
				self.dy = self.jumpingSpeed
				self.startFalling()
			# end if
		else:
			if jumpNum / self.maxChance == self.flyChance and self.dy <= 30:
				self.dy = self.flyUpSpeed
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
		super(Enemy, self).kill()
		
		pyglet.clock.schedule_once(self.respawn, 1.5)
	# end kill
	
	def checkPlayerCollision(self, p, dt):
		offset = 5
		if p.imgBottom <= self.imgTop and p.imgTop >= self.imgBottom and p.imgRight >= self.imgLeft and p.imgLeft <= self.imgRight:
			if p.y >= self.y - offset:
				self.kill()
				p.incScore()
			elif p.y < self.y - offset:
				p.kill()
			# end if
		# end if
	# end checkPlayerCollision
# end Enemy
