import pyglet
from gameObjects import physicalObject, resources, objects, util

class Spawner(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Spawner, self).__init__(img = resources.spawnerImage, *args, **kwargs)
		
		self.spawnX = self.x
		self.spawnY = (self.y + self.image.height / 2) + 20
		
		self.distances = [0] * 5
	# end __init__
	
	def update(self, dt):
		super(Spawner, self).update(dt)
		self.distanceToEntitys()
	# end update
	
	def distanceToEntitys(self):
		# first distance to player
		c = 0
		self.distances[c] = util.distanceTo((self.x, self.y), (objects.playerOne.x, objects.playerOne.y))
		c += 1
		# then distance to enemys in order they appear in their array
		for e in objects.enemys:
			self.distances[c] = util.distanceTo((self.x, self.y), (e.x, e.y))
			c += 1
		# end for
	# end distanceToEntitys
# end Spawner
