
class GameObject(object):
    SPEED = 10
    COLOR = 'black'

    def __init__(self, x, y, drawer):
        self.x = x
        self.y = y
        self.drawer = drawer

    def x_pos(self):
        return self.x

    def y_pos(self):
        return self.y
