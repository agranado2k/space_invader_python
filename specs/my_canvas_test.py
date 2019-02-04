import test_helper

from unittest import TestCase

from space_invaders.game import MyCanvas


class TestMyCanvas(TestCase):

    def test_canvas_width_and_height(self):
        self.assertIsNotNone(MyCanvas.HEIGHT)
        self.assertIsNotNone(MyCanvas.WIDTH)
