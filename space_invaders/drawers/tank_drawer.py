class TankDrawer(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, width, height, cannon_width, cannon_height, color):
        tank_begin_pos_x = x/2 - width/2
        tank_begin_pos_y = y - height
        tank_end_pos_x = x/2 + width/2
        tank_end_pos_y = y
        self.canvas.create_rectangle(tank_begin_pos_x,
                                     tank_begin_pos_y,
                                     tank_end_pos_x,
                                     tank_end_pos_y,
                                     fill=color)

        cannon_begin_pos_x = x/2 - cannon_width/2
        cannon_begin_pos_y = y - height - cannon_height
        cannon_end_pos_x = x/2 + cannon_width/2
        cannon_end_pos_y = y - height
        self.canvas.create_rectangle(cannon_begin_pos_x,
                                     cannon_begin_pos_y,
                                     cannon_end_pos_x,
                                     cannon_end_pos_y,
                                     fill=color)

