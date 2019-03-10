import threading
import time

from space_invaders.tank import Tank
from space_invaders.missile import Missile
from space_invaders.drawers.tank_drawer import TankDrawer
from space_invaders.drawers.missile_drawer import MissileDrawer

class MyCanvas(object):
    HEIGHT = 500
    WIDTH = 300


class Game(object):
    def __init__(self, canvas, width, height, is_redraw=True):
        self.is_redraw = is_redraw
        self.width = width
        self.setup(canvas, width, height)


    def setup(self, canvas, width, height):
        self.canvas = canvas
        self.the_tank = Tank(width/2, height, TankDrawer(canvas))
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
        self.move_objects()
        self.the_tank.draw()
        for missile in self.i_missiles:
            missile.draw()


    def objecst_in_canvas(self):
        return self.canvas.find_all()


    def invaders(self):
        return []


    def missiles(self):
        return self.i_missiles


    def tank(self):
        return self.the_tank

    def move_objects(self):
        for missile in self.i_missiles:
            missile.move()

    def move_tank_to_right(self):
        if self.is_tank_reached_right_edge():
            return

        self.the_tank.change_direction(Tank.RIGHT)
        self.the_tank.move()

    def is_tank_reached_right_edge(self):
        tank_right_limit = self.tank().x_pos() + Tank.WIDTH/2 - Tank.SPEED
        return tank_right_limit >= self.width

    def move_tank_to_left(self):
        if self.is_tank_reached_left_edge():
            return

        self.the_tank.change_direction(Tank.LEFT)
        self.the_tank.move()

    def is_tank_reached_left_edge(self):
        tank_left_limit = self.tank().x_pos() - Tank.WIDTH/2
        return tank_left_limit <= 0

    def tank_fire(self):
        missile_x = self.the_tank.x_pos() - Tank.CANNON_WIDTH/2
        missile_height = self.the_tank.y_pos() - Tank.CANNON_HEIGHT - Missile.HEIGHT
        missile = Missile.create(missile_x , missile_height, MissileDrawer(self.canvas))
        self.i_missiles.append(missile)
