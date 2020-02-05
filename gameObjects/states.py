import pyglet
from pyglet.window import key
from gameObjects import timer, objects

class States():
	def __init__(self, g):
		self.firstOpening = True
		self.endState = False
		
		self.player = objects.playerOne
		
		self.gameWindow = g
		
		self.playerDead = False
		self.playerLives = self.player.checkLives()
		self.playerScore = self.player.getScore()
		
		self.startGameLabel = pyglet.text.Label("PRESS ENTER TO START",
				   			font_name = "Times New Roman",
				   			font_size = 40,
				   			x = self.gameWindow.width // 2, y = self.gameWindow.height // 2,
				   			anchor_x = "center", anchor_y = "center")

		self.lostLifeLabel = pyglet.text.Label("PRESS ENTER TO RESPAWN",
				  		       font_name = "Times New Roman",
				  		       font_size = 40,
				  		       x = self.gameWindow.width // 2, y = self.gameWindow.height // 2,
				  		       anchor_x = "center", anchor_y = "center")

		self.endGameLabel = pyglet.text.Label("GAME OVER, PRESS ENTER TO RESTART", multiline = True, width = self.gameWindow.width,
					  	      font_name = "Times New Roman",
				 		      font_size = 40,
				 		      x = self.gameWindow.width // 2, y = self.gameWindow.height // 2,
				 		      anchor_x = "center", anchor_y = "center")
		
		self.clock = timer.Timer()
		self.maxTime = 30
		
		self.keyHandler = key.KeyStateHandler()
		self.eventHandlers = [self, self.keyHandler]
	# end __init__
	
	def update(self, dt):
		self.clock.tickClock(dt)
		
		self.playerDead = not self.player.visible
		self.playerLives = self.player.checkLives()
		self.playerScore = self.player.getScore()
		
		if self.clock.getTime() >= self.maxTime or self.playerLives == 0:
			self.endState = True
		# end if
	# end update
	
	def draw(self):
		self.clock.draw()
		if self.firstOpening:
			self.startGameLabel.draw()
			self.checkKeys()
		elif self.endState:
			self.endGameLabel.text = f"YOU FINISHED WITH A SCORE OF {self.playerScore}\nPRESS ENTER TO RESTART"
			self.endGameLabel.draw()
			self.checkKeys()
		elif self.playerDead:
			self.lostLifeLabel.draw()
			self.checkKeys()
		# end if
	# end update
	
	def checkKeys(self):
		if self.keyHandler[key.ENTER]:
			if self.firstOpening:
				self.firstOpening = False
				self.player.reset()
				self.player.startFalling()
			elif self.endState:
				self.endState = False
				self.clock.resetClock()
				self.player.resetScore()
				
				for e in objects.enemys:
					e.reset()
				# end for
				for l in objects.lives:
					l.visible = True
				# end for
				
				self.player.resetLives()
				self.player.reset()
				self.player.startFalling()
				self.playerDead = False
			elif self.playerDead:
				self.player.respawn()
				self.player.startFalling()
				self.playerDead = False
			# end if
		# end if
	# end checkKeys
# end States
