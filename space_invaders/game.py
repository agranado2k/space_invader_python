import threading
import time

from space_invaders.tank import Tank
from space_invaders.missile import Missile
from space_invaders.drawers.tank_drawer import TankDrawer

class MyCanvas(object):
    HEIGHT = 500
    WIDTH = 300


class Game(object):
    def __init__(self, canvas, width, height, is_redraw=True):
        self.is_redraw = is_redraw
        self.setup(canvas, width, height)


    def setup(self, canvas, width, height):
        self.canvas = canvas
        self.the_tank = Tank(width, height, TankDrawer(canvas))
        self.i_missiles = []

        self.interval_to_draw = 0.08
        thread = threading.Thread(target=self.clock, args=())
        thread.daemon = True
        thread.start()


    def clock(self):
        while self.is_redraw:
            self.redraw()
            # move all objects, except tank
            time.sleep(self.interval_to_draw)

        return 0


    def redraw(self):
        self.canvas.delete('all')
        self.the_tank.draw()
        # draw all missiles


    def objecst_in_canvas(self):
        return self.canvas.find_all()


    def invaders(self):
        return []


    def missiles(self):
        return self.i_missiles


    def tank(self):
        return self.the_tank


    def move_tank_to_right(self):
        self.the_tank.change_direction(Tank.RIGHT)
        self.the_tank.move()


    def move_tank_to_left(self):
        self.the_tank.change_direction(Tank.LEFT)
        self.the_tank.move()


    def tank_fire(self):
        missile = Missile.create(self.the_tank.x_pos(), self.the_tank.y_pos())
        self.i_missiles.append(missile)
