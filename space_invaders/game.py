
from tkinter import Tk, Canvas
from space_invaders.tank import Tank

class MyCanvas(object):
    HEIGHT = 500
    WIDTH = 300


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


class Game(object):
    def __init__(self, canvas, width, height):
        self.setup(canvas, width, height)

    def setup(self, canvas, width, height):
        self.the_tank = Tank(width, height, TankDrawer(canvas))
        # self.the_tank.draw()

    def clock(self):
        return 0

    def invaders(self):
        return []

    def missiles(self):
        return []

    def tank(self):
        return self.the_tank

master = Tk()
master.title( "Space Invanders" )
canvas = Canvas(master, height=MyCanvas.HEIGHT, width=MyCanvas.WIDTH)
canvas.pack()
Game(canvas, MyCanvas.WIDTH, MyCanvas.HEIGHT)
master.mainloop()
