import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from tkinter import Tk, Canvas
from space_invaders.game import Game, TankDrawer, MyCanvas
from space_invaders.tank import *


class TestGame(TestCase):
    def setUp(self):
        canvas = MagicMock()
        self.game = Game(canvas, MyCanvas.WIDTH, MyCanvas.HEIGHT)


    def test_initial_game_state(self):
        self.assertEqual(self.game.clock(), 0)
        self.assertEqual(len(self.game.invaders()), 0)
        self.assertEqual(len(self.game.missiles()), 0)
        self.assertIsInstance(self.game.tank(), Tank)

