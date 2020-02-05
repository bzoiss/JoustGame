import pyglet


class Timer():
	def __init__(self):
		self.time = 0.0
		
		self.timeLabel = pyglet.text.Label("0.00 s",
						   font_name = "Times New Roman",
						   font_size = 20,
						   x = 50, y = 570,
						   anchor_x = "center", anchor_y = "center")
	# end __init__
	
	def draw(self):
		self.timeLabel.text = f"{self.time:.2f} s"
		self.timeLabel.draw()
	# end draw
	
	def tickClock(self, dt):
		self.time += dt
	# end tickClock

	def resetClock(self):
		self.time = 0.00
	# end resetClock
	
	def getTime(self):
		return self.time
	# end getTime
# end Timer
