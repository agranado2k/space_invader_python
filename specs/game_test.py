from unittest import TestCase
from unittest.mock import MagicMock


class TestGame(TestCase):
    WIDTH = 120
    HEIGHT = 300

    def setUp(self):
        interface = MagicMock()
        self.game = Game(interface, self.WIDTH, self.HEIGHT)


    def test_initial_game_state(self):
        self.assertEqual(self.game.clock(), 0)
        self.assertEqual(len(self.game.invaders()), 0)
        self.assertEqual(len(self.game.missiles()), 0)
        self.assertIsInstance(self.game.tank(), Tank)


class TestTank(TestCase):
    WIDTH = 120

    def setUp(self):
        self.tank = Tank(self.WIDTH/2, 0)

    def test_tank_initial_position(self):
        self.assertEqual(self.tank.x_pos(), self.WIDTH/2)
        self.assertEqual(self.tank.y_pos(), 0)
        self.assertEqual(self.tank.direction(), Tank.RIGHT)


class Tank(object):
    RIGHT = 0

    def __init__(self, x, y):
        self.x = x

    def x_pos(self):
        return self.x

    def y_pos(self):
        return 0

    def direction(self):
        return self.RIGHT


class Game(object):
    def __init__(self, inteface, width, height):
        self.the_tank = Tank(width/2, 0)

    def clock(self):
        return 0

    def invaders(self):
        return []

    def missiles(self):
        return []

    def tank(self):
        return self.the_tank

