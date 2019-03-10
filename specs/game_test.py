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

    @patch('space_invaders.game.Game.is_tank_reached_right_edge', return_value=False)
    def test_move_tank_to_right(self, mock_is_tank_reached_right_edge):
        self.game.move_tank_to_right()

        mock_is_tank_reached_right_edge.assert_called_once()
        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH/2 + Tank.SPEED)

    def test_limit_tank_moviment_to_right_to_canvas_edge(self):
        for i in range(100):
            self.game.move_tank_to_right()

        self.assertTrue(self.game.is_tank_reached_right_edge())

    @patch('space_invaders.game.Game.is_tank_reached_left_edge', return_value=False)
    def test_move_tank_to_left(self, mock_is_fank_reached_left_edge):
        self.game.move_tank_to_left()

        mock_is_fank_reached_left_edge.assert_called_once()
        self.assertEqual(self.game.tank().x_pos(), MyCanvas.WIDTH/2 - Tank.SPEED)

    def test_limit_tank_moviment_to_left_to_canvas_edge(self):
        for i in range(100):
            self.game.move_tank_to_left()

        self.assertTrue(self.game.is_tank_reached_left_edge())

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
