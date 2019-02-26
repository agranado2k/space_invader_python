import test_helper

from unittest import TestCase
from unittest.mock import MagicMock, patch

from space_invaders.missile import Missile
from space_invaders.drawers.missile_drawer import MissileDrawer


class TestMissile(TestCase):
    def setUp(self):
        canvas = MagicMock()
        self.drawer = MissileDrawer(canvas)


    def test_create_missile(self):
        cannon_x = 10
        cannon_y = 30

        missile = Missile.create(cannon_x, cannon_y, self.drawer)

        self.assertEqual(missile.x_pos(), cannon_x)
        self.assertEqual(missile.y_pos(), cannon_y)


    @patch('space_invaders.drawers.missile_drawer.MissileDrawer.draw')
    def test_draw_sending_message_to_drawer(self, mock_drawer_draw):
        cannon_x = 10
        cannon_y = 30

        missile = Missile.create(cannon_x, cannon_y, self.drawer)

        missile.draw()

        mock_drawer_draw.assert_called_once_with(cannon_x,
                                                 cannon_y,
                                                 cannon_x + Missile.WIDTH,
                                                 cannon_y + Missile.HEIGHT,
                                                 Missile.COLOR)
