import pyglet
from gameObjects import resources

class PhysicalObject(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		
		self.dx, self.dy = 0.0, 0.0
		self.ddx, self.ddy = 0.0, 0.0
		
		self.imgBottom = 0
		self.imgTop = 0
		self.imgRight = 0
		self.imgLeft = 0
	# end init
	
	def update(self, dt):
		self.updateImgBounds()
		
		self.dx += self.ddx * dt
		self.dy += self.ddy * dt
		
		self.x += self.dx * dt
		self.y += self.dy * dt
	# end update
	
	def updateImgBounds(self):
		self.imgBottom = self.y - self.image.height / 2
		self.imgTop = self.y + self.image.height / 2
		self.imgRight = self.x + self.image.width / 2
		self.imgLeft = self.x - self.image.width / 2
	# end updateImgBounds
# end PhysicalObject
