import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from tkinter import Tk, Canvas
from space_invaders.missile import Missile
from space_invaders.drawers.missile_drawer import MissileDrawer
from space_invaders.game import MyCanvas


class TestMissileDrawer(TestCase):
    def setUp(self):
        master = Tk()
        self.pos_x = 30
        self.pos_y = 100
        canvas = Canvas(master, height=MyCanvas.HEIGHT, width=MyCanvas.WIDTH)
        drawer = MissileDrawer(canvas)
        self.missile = Missile(self.pos_x, self.pos_y, drawer)


    @patch('tkinter.Canvas.create_rectangle')
    def test_draw_missile_on_position(self, create_rectangle_mock):
        self.missile.draw()

        create_rectangle_mock.assert_any_call(self.pos_x,
                                              self.pos_y,
                                              self.pos_x + Missile.HEIGHT,
                                              self.pos_y + Missile.WIDTH,
                                              fill=Missile.COLOR)
