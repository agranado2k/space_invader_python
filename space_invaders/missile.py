
class Missile(object):
    HEIGHT = 15
    WIDTH = 30
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


    def draw(self):
        self.drawer.draw(self.pos_x,
                         self.pos_y,
                         self.pos_x + self.WIDTH,
                         self.pos_y + self.HEIGHT,
                         self.COLOR)
