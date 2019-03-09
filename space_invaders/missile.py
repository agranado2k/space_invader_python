from space_invaders.game_object import GameObject

class Missile(GameObject):
    HEIGHT = 5
    WIDTH = 10

    def move(self):
        self.y -= self.SPEED

    def create(x, y, drawer):
        return Missile(x, y, drawer)

    def draw(self):
        self.drawer.draw(self.x,
                         self.y,
                         self.x + self.HEIGHT,
                         self.y + self.WIDTH,
                         self.COLOR)
