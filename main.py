import pyglet
from pyglet.window import key
from gameObjects import objects, timer, states

# primary window
gameWindow = pyglet.window.Window(width = 800, height = 600, caption = "Jouster")

# sprite batches
platformBatch = objects.platformBatch
spawnerBatch = objects.spawnerBatch
enemyBatch = objects.enemyBatch
playerLivesBatch = objects.playerLivesBatch

# all game objects
lava = objects.lava

background = objects.background

playerOne = objects.playerOne

enemys = objects.enemys

spawners = objects.spawners

platforms = objects.platforms

lives = objects.lives

stateManager = states.States(gameWindow)

# pushing key handlers to objects
gameWindow.push_handlers(playerOne.keyHandler)
gameWindow.push_handlers(stateManager.keyHandler)

@gameWindow.event
def on_draw():
	gameWindow.clear()
	background.draw()
	if not stateManager.playerDead:
		playerOne.draw()
		for i in range(0, len(lives) - playerOne.checkLives()):
			lives[i].visible = False
		# end for
	# end if
	enemyBatch.draw()
	lava.draw()
	platformBatch.draw()
	spawnerBatch.draw()
	stateManager.draw()
	for l in lives:
		l.draw()
	# end for
	playerOne.drawScore()
# end draw

def update(dt):
	for s in spawners:
		s.update(dt)
	# end for
	if not stateManager.playerDead and not stateManager.endState:
		playerOne.update(dt)
		for p in platforms:
			p.update(dt)
		# end for
		for e in enemys:
			if e.visible:
				e.update(dt)
			# end if
		# end for
		stateManager.update(dt)
		checkCollisions(dt)
		playerOne.checkFalling()
	# end if
	stateManager.update(0)
# end update

def checkCollisions(dt):
	for p in platforms:
		p.checkPlayerCollision(playerOne, dt)
		for e in enemys:
			p.checkPlayerCollision(e, dt)
		# end for
	# end for
	for e in enemys:
		if e.visible:
			e.checkPlayerCollision(playerOne, dt)
		# end if
	# end for
# end checkCollisions

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1 / 120.0)	
	
	pyglet.app.run()
# end main if
