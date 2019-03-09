import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from tkinter import Tk, Canvas
from space_invaders.game import Game, TankDrawer, MyCanvas
from space_invaders.tank import Tank
from space_invaders.missile import Missile


class TestGame(TestCase):
    def setUp(self):
        canvas = MagicMock()
        self.game = Game(canvas, MyCanvas.WIDTH, MyCanvas.HEIGHT, is_redraw=False)


    def test_initial_game_state(self):
        self.assertEqual(self.game.clock(), 0)
        self.assertEqual(len(self.game.invaders()), 0)
        self.assertEqual(len(self.game.missiles()), 0)
        self.assertIsInstance(self.game.tank(), Tank)


    @patch('space_invaders.game.Game.move_objects')
    @patch('space_invaders.missile.Missile.draw')
    @patch('space_invaders.tank.Tank.draw')
    def test_game_have_to_redraw_all_objects(self, mock_tank_draw, mock_missile_draw, mock_move_objects):
        self.game.tank_fire()

        self.game.redraw()

        mock_tank_draw.assert_called_once()
        mock_missile_draw.assert_called_once()
        mock_move_objects.assert_called_once()

    def test_move_tank_to_right(self):
        self.game.move_tank_to_right()

        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH/2 + Tank.SPEED)


    def test_move_tank_to_left(self):
        self.game.move_tank_to_left()

        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH/2 - Tank.SPEED)

    def test_tank_fire_missile(self):
        self.game.tank_fire()

        missile = self.game.missiles()[0]
        self.assertEqual(len(self.game.missiles()), 1)
        self.assertEqual(missile.x_pos(), self.game.tank().x_pos() - Tank.CANNON_WIDTH/2)
        self.assertEqual(missile.y_pos(), self.game.tank().y_pos() - Tank.CANNON_HEIGHT - Missile.HEIGHT)

    def test_move_objects(self):
        self.game.tank_fire()

        self.game.move_objects()

        missile = self.game.missiles()[0]
        expected_position = self.game.tank().y_pos() - Tank.CANNON_HEIGHT - Missile.HEIGHT - Missile.SPEED
        self.assertEqual(missile.y_pos(), expected_position)
