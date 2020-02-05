import pyglet
from gameObjects import physicalObject, resources, util

class Platform(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Platform, self).__init__(img = resources.platformImage, *args, **kwargs)
	# end init
	
	def update(self, dt):
		super(Platform, self).update(dt)
	# end update
	
	def checkPlayerCollision(self, p, dt):
		if p.isFalling():
			if p.imgBottom <= self.imgTop and p.imgRight <= self.imgLeft and p.imgTop >= self.imgBottom:
				nextPosRight = p.x + p.dx * dt
				nextPosRight += p.image.width / 2
				if nextPosRight >= self.imgLeft:
					p.dx = 0
				# end if
			elif p.imgBottom <= self.imgTop and p.imgLeft >= self.imgRight and p.imgTop >= self.imgBottom:
				nextPosLeft = p.x + p.dx * dt
				nextPosLeft -= p.image.width / 2
				if nextPosLeft <= self.imgRight:
					p.dx = 0
				# end if
			# end if
			# velocity downward
			if p.dy < 0:
				if p.imgBottom <= self.imgTop and p.imgTop >= self.imgBottom and (p.imgRight >= self.imgLeft and p.imgLeft <= self.imgRight):
					p.endFalling(self)
				# end if
			# velocity upward
			elif p.dy > 0:
				if p.imgTop <= self.imgBottom and (p.imgRight >= self.imgLeft and p.imgLeft <= self.imgRight):
					nextPosUp = p.y + p.dy * dt
					nextPosUp += p.image.height / 2
					if nextPosUp >= self.imgBottom:
						p.dy = 0
						p.startFalling()
					# end if
				# end if
			# end if
		# end if
	# end checkPlayerCollision
# end Platform
