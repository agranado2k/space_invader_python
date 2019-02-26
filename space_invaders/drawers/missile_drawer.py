class MissileDrawer(object):
    def __init__(self, canvas):
        self.canvas = canvas


    def draw(self, mb_pos_x, mb_pos_y, me_pos_x, me_pos_y, color):
        self.canvas.create_rectangle(mb_pos_x,
                                     mb_pos_y,
                                     me_pos_x,
                                     me_pos_y,
                                     fill=color)
