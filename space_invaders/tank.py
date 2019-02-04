
RIGHT = 'right'
LEFT = 'left'
COLOR = 'black'
HEIGHT = 15
WIDTH = 35
RIGHT = 0
CANNON_WIDTH=10
CANNON_HEIGHT=10
SPEED = 10

class Tank(object):

    def __init__(self, x, y, drawer):
        self.x = x
        self.y = y
        self.drawer = drawer

    def x_pos(self):
        return self.x

    def y_pos(self):
        return self.y

    def direction(self):
        return RIGHT

    def change_direction(self, direct):
        self.direction = direct

    def move(self):
        self.x += SPEED

    def draw(self):
        self.drawer.draw(self.x,
                         self.y,
                         WIDTH,
                         HEIGHT,
                         CANNON_WIDTH,
                         CANNON_HEIGHT,
                         COLOR)

