import pyglet
from gameObjects import physicalObject, objects

class Entity(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Entity, self).__init__(*args, **kwargs)
		
		self.moveSpeed = 300.0
		self.moveDir = 0
		self.fallingSpeed = -500.0
		self.dragFactor = 20.0
		self.jumpingSpeed = 375.0
		self.flyUpSpeed = 250.0
		
		self.initX = self.x
		self.initY = self.y
		
		self.falling = False
		
		self.spawner = None
	# end __init__
	
	def update(self, dt):
		super(Entity, self).update(dt)
		self.spawner = self.findSpawner()
	# end update
	
	def isFalling(self):
		return self.falling
	# end isFalling
	
	def startFalling(self):
		self.falling = True
		self.ddy = self.fallingSpeed
	# end startFalling
	
	def endFalling(self, p):
		self.falling = False
		self.ddy = 0
		self.dy = 0
		self.y = p.imgTop + self.image.height / 2
	# end endFalling
	
	def checkFalling(self):
		if self.imgBottom == 37.5:
			if self.imgRight <= 150 or self.imgLeft >= 650:
				self.startFalling()
			# end if
		elif self.imgBottom == 162.5:
			if self.imgRight <= 550 and self.imgLeft >= 250:
				self.startFalling()
			# end if
		elif self.imgBottom == 287.5:
			if self.imgRight <= 150 or self.imgLeft >= 650:
				self.startFalling()
			# end if
		elif self.imgBottom == 412.5:
			if self.imgRight <= 550 and self.imgLeft >= 250:
				self.startFalling()
			# end if
		# end if
	# end checkFalling
	
	def kill(self):
		self.visible = False
		self.ddx = 0
		self.ddy = 0
		self.dx = 0
		self.dy = 0
	# end kill
	
	def reset(self):
		self.ddy = 0
		self.ddx = 0
		self.dy = 0
		self.dx = 0
		self.x = self.initX
		self.y = self.initY
		self.visible = True
	# end reset
	
	def respawn(self, dt = 0):
		self.x = self.spawner.spawnX
		self.y = self.spawner.spawnY
		self.visible = True
	# end respawn
	
	def findSpawner(self):
		maxDist = 0
		spawn = objects.spawners[0]
		for s in objects.spawners:
			currentDist = 0
			for i in range(5):
				currentDist += s.distances[i]
			# end for
			if currentDist / 5 > maxDist:
				spawn = s
				maxDist = currentDist / 5
			# end if
		# end for
		return spawn
	# end findSpawner
# end Entity
