import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from space_invaders.missile import Missile
from space_invaders.drawers.missile_drawer import MissileDrawer


class TestMissile(TestCase):
    def setUp(self):
        canvas = MagicMock()
        self.drawer = MissileDrawer(canvas)
        self.cannon_x = 35
        self.cannon_y = 50
        self.missile = Missile.create(self.cannon_x, self.cannon_y, self.drawer)


    def test_create_missile(self):
        self.assertEqual(self.missile.x_pos(), self.cannon_x)
        self.assertEqual(self.missile.y_pos(), self.cannon_y)


    @patch('space_invaders.drawers.missile_drawer.MissileDrawer.draw')
    def test_draw_sending_message_to_drawer(self, mock_drawer_draw):
        self.missile.draw()

        mock_drawer_draw.assert_called_once_with(self.cannon_x,
                                                 self.cannon_y,
                                                 self.cannon_x + Missile.HEIGHT,
                                                 self.cannon_y + Missile.WIDTH,
                                                 Missile.COLOR)

    def test_move_itself(self):
        initial_x_pos = self.missile.x_pos()
        initial_y_pos = self.missile.y_pos()

        self.missile.move()

        self.assertEquals(self.missile.x_pos(), initial_x_pos)
        self.assertEquals(self.missile.y_pos(), initial_y_pos - Missile.SPEED)
