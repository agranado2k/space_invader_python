
class Missile(object):
    HEIGHT = 15

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


    def create(pos_x, pos_y):
        return Missile(pos_x, pos_y + Missile.HEIGHT)


    def x_pos(self):
        return self.pos_x


    def y_pos(self):
        return self.pos_y
