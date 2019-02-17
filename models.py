import arcade
from coldetect import check_player_pillar_collision

class Player:
    STATE_FROZEN = 1
    STATE_STARTED = 2
    GRAVITY = 1
    STARTING_VELOCITY = 15
    JUMPING_VELOCITY = 15

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vy = Player.STARTING_VELOCITY
 
    def update(self, delta):
        self.y += self.vy
        self.vy -= Player.GRAVITY

    def jump(self):
        self.vy = Player.JUMPING_VELOCITY
 
class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(self, width // 2, height // 2)
        self.state = World.STATE_FROZEN
        self.pillar_pair = PillarPair(self, width - 100, height // 2)
 
    def update(self, delta):
        if self.state == World.STATE_FROZEN:
            return 
        self.player.update(delta)
        self.vy = Player.STARTING_VELOCITY
        self.pillar_pair.update(delta)

        if self.pillar_pair.hit(self.player):
            self.state = self.STATE_FROZEN
            self.player.x = 


    def on_key_press(self, key, key_modifiers):
        self.player.jump()

    def start(self):
        self.state = World.STATE_STARTED
 
    def freeze(self):
        self.state = World.STATE_FROZEN     
 
    def is_started(self):
        return self.state == World.STATE_STARTED



class PillarPair:
    PILLAR_SPEED = 5

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        self.x -= PillarPair.PILLAR_SPEED

        if self.x == -20:
            self.x = 800
    
    def hit(self, player):
        return check_player_pillar_collision(player.x, player.y,
                                             self.x, self.y)

