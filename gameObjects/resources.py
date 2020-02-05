import pyglet

def centerImage(img):
	img.anchor_x = img.width / 2
	img.anchor_y = img.height / 2
# end centerImage

# set image path
pyglet.resource.path = ["resources/"]
pyglet.resource.reindex()

# make image and center the anchor points
playerImageRight = pyglet.resource.image("playerRight.png")
centerImage(playerImageRight)

playerImageLeft = pyglet.resource.image("playerLeft.png")
centerImage(playerImageLeft)
	
platformImage = pyglet.resource.image("platform.png")
centerImage(platformImage)

backgroundImage = pyglet.resource.image("background.png")
centerImage(backgroundImage)

lavaImage = pyglet.resource.image("lava.png")
centerImage(lavaImage)

enemyImageRight = pyglet.resource.image("enemyRight.png")
centerImage(enemyImageRight)

enemyImageLeft = pyglet.resource.image("enemyLeft.png")
centerImage(enemyImageLeft)

spawnerImage = pyglet.resource.image("spawner.png")
centerImage(spawnerImage)
