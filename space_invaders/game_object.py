
class GameObject(object):
    SPEED = 10
    COLOR = 'black'

    def __init__(self, x, y, drawer):
        self.x = x
        self.y = y
        self.drawer = drawer

    def speed(self):
        return self.SPEED

    def x_pos(self):
        return self.x

    def set_x_pos(self, value):
        self.x = value

    def y_pos(self):
        return self.y
