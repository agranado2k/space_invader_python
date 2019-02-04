import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from tkinter import Tk, Canvas
from space_invaders.tank import Tank
from space_invaders.game import TankDrawer, MyCanvas


class TestTankDrawer(TestCase):
    def setUp(self):
        master = Tk()
        canvas = Canvas(master, height=MyCanvas.HEIGHT, width=MyCanvas.WIDTH)
        drawer = TankDrawer(canvas)
        self.tank = Tank(MyCanvas.WIDTH, MyCanvas.HEIGHT, drawer)

    @patch('tkinter.Canvas.create_rectangle')
    def test_draw_tank_on_initial_position(self, create_rectangle_mock):
        self.tank.draw()

        create_rectangle_mock.assert_any_call(MyCanvas.WIDTH/2 - Tank.WIDTH/2,
                                              MyCanvas.HEIGHT - Tank.HEIGHT,
                                              MyCanvas.WIDTH/2 + Tank.WIDTH/2,
                                              MyCanvas.HEIGHT,
                                              fill=Tank.COLOR)
        create_rectangle_mock.assert_any_call(MyCanvas.WIDTH/2 - Tank.CANNON_WIDTH/2,
                                              MyCanvas.HEIGHT - Tank.HEIGHT - Tank.CANNON_HEIGHT,
                                              MyCanvas.WIDTH/2 + Tank.CANNON_WIDTH/2,
                                              MyCanvas.HEIGHT - Tank.HEIGHT,
                                              fill=Tank.COLOR)
