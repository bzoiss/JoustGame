# Joust Inspired Game

## Run Instructions:
	$pip install pyglet (note: must be using Python 3)
	$python main.py

## Documentation:
### main.py:
- all game objects and state control variables are declared
- methods: on_draw(), update(dt), checkCollisions(dt)
- on_draw(): will draw the layers based on the state variables
- update(dt): called after scheduled at the start of the program.  Calls updates on other objects depending on state variables and calls checkCollision(dt)
- checkCollisions(dt): checks for collisions of player/enemy with platforms and player with enemys

### states.py
- an objects to keep track of states rather than doing it in the main
- methods: update(dt), draw(), checkKeys()
- update(dt): ticks the clock, updates the player variables, and checks for the end of the game
- draw(): draws the clock and the labels depending on the state variables
- checkKeys(): updates the state variables depending on the state variables

### timer.py
- holds a timer that uses a given dt to manipulate it
- methods: draw(), tickClock(dt), resetClock(), getTime()
- draw(): updates the time on the label and draws it on the screen
- tickClock(dt): adds the given dt to the current time
- resetClock(): resets the current time to 0
- getTime(): returns the current time

### physicalObject.py:
- the base class for all game objects
- methods: update(dt), updateImgBounds()
- update(dt): increments velocity and position accounting for dt
- updateImgBounds(): updates the bounds of the given image

### platform.py
- the class to keep track of a platform, inherits from PhysicalObject
- methods: update(dt), checkPlayerCollision()
- update(dt): calls the super class update(dt)
- checkPlayerCollision(p, dt): given an entity and dt it will check for collision with the platform and prevents it by setting the dy/dx to 0

### spawner.py
- the class to keep track of a spawner, inherits from PhysicalObject
- methods: update(dt), distanceToEntitys()
- update(dt): calls the super class update(dt) and updates the distances to all moving entitys
- distanceToEntitys(): calculates the distances to each movable entity

### entity.py
- the base class for the player and enemy, inherits from PhysicalObject
- methods: update(dt), isFalling(), startFalling(), endFalling(p), checkFalling(), kill(), reset(), respawn(dt), findSpawner()
- update(dt): calls the super class update(dt)
- isFalling(): returns true if the entity is falling and false if it is not
- startFalling(): sets the ddy to the falling speed and changes falling to true
- endFalling(p): ends falling on a given platform
- checkFalling(): checks if the entity should be falling
- kill(): makes the entity invisible and sets all movement values to 0
- reset(): resets the entity to it's initial position
- respawn(dt): respawns the entity at the decided spawner
- findSpawner(): finds the furthest average spawner from the entitys

### player.py
- the player class that the user controls, inherits from Entity
- methods: update(dt), checkBounds(dt), kill(), checkLives(), decLives(), resetLives(), incScore(), resetScore(), getScore(), drawScore()
- update(dt): calls the super class update(dt) and changes dy and dx values based on player input
- checkBounds(dt): makes sure the player obeys the bounds of the screen; top is a bounce, sides are wrap, and bottom is death
- kill(): calls the super class kill method, reduces lives by 1
- checkLives(): returns the number of lives the player has
- decLives(): reduces the player lives by 1 if it isn't already 0
- resetLives(): sets the current lives to the maximum lives
- incScore(): increments the score by 1
- resetScore(): resets the score to 0
- getScore(): returns the current score
- drawScore(): updates the score label text and draws it on the screen

### enemy.py
- the enemy class that opposes the player, inherits from Entity
- methods: update(dt), checkBounds(dt), kill(), checkPlayerCollision(p, dt)
- update(dt): calls the super class update(dt), sets the dx in a random direction based on the movespeed of the player and an offset, and randomly jumps/flys
- checkBonds(dt): very similar to player
- kill(): calls the super class kill method and sets a timer on respawn
- checkPlayerCollision(p, dt): given player collision and a dt, finds if a player collides with the enemy and decides to die or kill the player

### resources.py
- creates a path for all resources in the game
- creates all images used and centers their anchor points

### util.py
- utility methods, currently holds a distance function given 2 numbers
