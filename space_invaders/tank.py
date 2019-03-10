from space_invaders.game_object import GameObject

class Tank(GameObject):
    HEIGHT = 15
    WIDTH = 35
    RIGHT = 'Right'
    LEFT = 'Left'
    CANNON_WIDTH=10
    CANNON_HEIGHT=10

    def __init__(self, x, y, drawer):
        GameObject.__init__(self, x, y, drawer)
        self._direction = self.RIGHT

    def move(self):
        self.set_x_pos(self.x_pos() + self.tank_speed())

    def tank_speed(self):
        speed = self.speed()
        if self._direction == self.LEFT:
            speed *= -1

        return speed

    def direction(self):
        return self._direction

    def change_direction(self, direct):
        self._direction = direct

    def draw(self):
        self.drawer.draw(self.x_pos(),
                         self.y_pos(),
                         self.WIDTH,
                         self.HEIGHT,
                         self.CANNON_WIDTH,
                         self.CANNON_HEIGHT,
                         self.COLOR)

