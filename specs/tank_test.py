import test_helper

from unittest import TestCase
from unittest.mock import MagicMock

from space_invaders.game import TankDrawer, MyCanvas
from space_invaders.tank import Tank


class TestTank(TestCase):
    def setUp(self):
        canvas = MagicMock()
        drawer = TankDrawer(canvas)
        self.tank = Tank(MyCanvas.WIDTH/2, MyCanvas.HEIGHT, drawer)


    def test_tank_initial_position(self):
        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2)
        self.assertEqual(self.tank.y_pos(), MyCanvas.HEIGHT)
        self.assertEqual(self.tank.direction(), Tank.RIGHT)


    def test_tank_change_directin(self):
        self.tank.change_direction(Tank.LEFT)

        self.assertEqual(self.tank.direction(), Tank.LEFT)


    def test_tank_move_to_right(self):
        self.tank.change_direction(Tank.RIGHT)

        self.tank.move()

        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2 + Tank.SPEED)


    def test_tank_move_to_left(self):
        self.tank.change_direction(Tank.LEFT)

        self.tank.move()

        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2 - Tank.SPEED)
