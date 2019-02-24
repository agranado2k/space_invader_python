import test_helper

from unittest import TestCase
# from unittest.mock import MagicMock, patch

# from space_invaders.game import MyCanvas
from space_invaders.missile import Missile


class TestTank(TestCase):
    def setUp(self):
        pass
        # canvas = MagicMock()
        # drawer = TankDrawer(canvas)

    def test_create_missile(self):
        cannon_x = 10
        cannon_y = 30

        missile = Missile.create(cannon_x, cannon_y)

        self.assertEqual(missile.x_pos(), cannon_x)
        self.assertEqual(missile.y_pos(), cannon_y + Missile.HEIGHT)
