import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from space_invaders.game import TankDrawer, MyCanvas
import space_invaders.tank as tank


class TestTank(TestCase):
    def setUp(self):
        canvas = MagicMock()
        drawer = TankDrawer(canvas)
        self.tank = tank.Tank(MyCanvas.WIDTH/2, MyCanvas.HEIGHT, drawer)

    def test_tank_initial_position(self):
        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2)
        self.assertEqual(self.tank.y_pos(), MyCanvas.HEIGHT)
        self.assertEqual(self.tank.direction(), tank.RIGHT)

    def test_tank_change_directin(self):
        self.tank.change_direction(tank.LEFT)

        self.assertEqual(self.tank.direction(), tank.LEFT)

    def test_tank_move_to_right(self):
        self.tank.change_direction(tank.RIGHT)

        self.tank.move()

        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2 + tank.SPEED)

    def test_tank_move_to_left(self):
        self.tank.change_direction(tank.LEFT)

        self.tank.move()

        self.assertEqual(self.tank.x_pos(), MyCanvas.WIDTH/2 - tank.SPEED)
