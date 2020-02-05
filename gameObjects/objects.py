import pyglet
from gameObjects import player, platform, resources, enemy, spawner

platformBatch = pyglet.graphics.Batch()
spawnerBatch = pyglet.graphics.Batch()
enemyBatch = pyglet.graphics.Batch()
playerLivesBatch = pyglet.graphics.Batch()

# game object declaration
lava = pyglet.sprite.Sprite(img = resources.lavaImage, x = 400, y = 14)

background = pyglet.sprite.Sprite(img = resources.backgroundImage, x = 400, y = 300)

playerOne = player.Player(x = 400, y = 325)

enemys = []
enemys.append(enemy.Enemy(x = 100, y = 200, batch = enemyBatch))
enemys.append(enemy.Enemy(x = 200, y = 450, batch = enemyBatch))
enemys.append(enemy.Enemy(x = 650, y = 200, batch = enemyBatch))
enemys.append(enemy.Enemy(x = 550, y = 450, batch = enemyBatch))

spawners = []
spawners.append(spawner.Spawner(x = 400, y = 283.5, batch = spawnerBatch))
spawners.append(spawner.Spawner(x = 650, y = 408.5, batch = spawnerBatch))
spawners.append(spawner.Spawner(x = 150, y = 408.5, batch = spawnerBatch))
spawners.append(spawner.Spawner(x = 650, y = 158.5, batch = spawnerBatch))
spawners.append(spawner.Spawner(x = 150, y = 158.5, batch = spawnerBatch))
spawners.append(spawner.Spawner(x = 400, y = 33.5, batch = spawnerBatch))

platforms = []
platforms.append(platform.Platform(x = 400, y = 25, batch = platformBatch))
platforms.append(platform.Platform(x = 0, y = 150, batch = platformBatch))
platforms.append(platform.Platform(x = 800, y = 150, batch = platformBatch))
platforms.append(platform.Platform(x = 400, y = 275, batch = platformBatch))
platforms.append(platform.Platform(x = 0, y = 400, batch = platformBatch))
platforms.append(platform.Platform(x = 800, y = 400, batch = platformBatch))

lives = []
lives.append(player.Player(x = 360, y = 20, batch = playerLivesBatch, vis = True, scale = .5))
lives.append(player.Player(x = 400, y = 20, batch = playerLivesBatch, vis = True, scale = .5))
lives.append(player.Player(x = 440, y = 20, batch = playerLivesBatch, vis = True, scale = .5))
