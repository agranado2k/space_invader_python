import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from tkinter import Tk, Canvas
from space_invaders.game import Game, TankDrawer, MyCanvas
from space_invaders.tank import Tank


class TestGame(TestCase):
    def setUp(self):
        canvas = MagicMock()
        self.game = Game(canvas, MyCanvas.WIDTH, MyCanvas.HEIGHT, is_redraw=False)


    def test_initial_game_state(self):
        self.assertEqual(self.game.clock(), 0)
        self.assertEqual(len(self.game.invaders()), 0)
        self.assertEqual(len(self.game.missiles()), 0)
        self.assertIsInstance(self.game.tank(), Tank)


    def test_move_tank_to_right(self):
        self.game.move_tank_to_right()

        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH + Tank.SPEED)


    def test_move_tank_to_left(self):
        self.game.move_tank_to_left()

        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH - Tank.SPEED)


    def test_tank_fire_missile(self):
        self.game.tank_fire()

        self.assertEqual(len(self.game.missiles()), 1)

