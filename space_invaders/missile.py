
class Missile(object):
    SPEED = 10
    HEIGHT = 5
    WIDTH = 10
    COLOR = 'black'

    def __init__(self, pos_x, pos_y, drawer):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.drawer = drawer


    def create(pos_x, pos_y, drawer):
        return Missile(pos_x, pos_y, drawer)


    def x_pos(self):
        return self.pos_x


    def y_pos(self):
        return self.pos_y

    def move(self):
        self.pos_y -= self.SPEED

    def draw(self):
        self.drawer.draw(self.pos_x,
                         self.pos_y,
                         self.pos_x + self.HEIGHT,
                         self.pos_y + self.WIDTH,
                         self.COLOR)
