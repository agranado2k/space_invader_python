
class Tank(object):

    RIGHT = 'Right'
    LEFT = 'Left'
    COLOR = 'black'
    HEIGHT = 15
    WIDTH = 35
    CANNON_WIDTH=10
    CANNON_HEIGHT=10
    SPEED = 10

    def __init__(self, x, y, drawer):
        self.x = x
        self.y = y
        self.drawer = drawer
        self._direction = self.RIGHT


    def x_pos(self):
        return self.x


    def y_pos(self):
        return self.y


    def direction(self):
        return self._direction


    def change_direction(self, direct):
        self._direction = direct


    def move(self):
        speed = self.SPEED
        if self._direction == self.LEFT:
            speed *= -1

        self.x += speed


    def draw(self):
        self.drawer.draw(self.x,
                         self.y,
                         self.WIDTH,
                         self.HEIGHT,
                         self.CANNON_WIDTH,
                         self.CANNON_HEIGHT,
                         self.COLOR)

