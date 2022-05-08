"""Unit test of main program."""

import unittest
import main


class TestMain(unittest.TestCase):

  def setUp(self):
    super().setUp()

  def test_make_coffee(self):
    expected_steps = '\n'.join([
        'Boil some water',
        'Brew coffee in boiling water',
        'Pour coffee in cup',
        'Add sugar and milk',
    ])

    real_steps = main.make_coffee()

    self.assertEqual(real_steps, expected_steps)

  def test_make_tea(self):
    expected_steps = '\n'.join([
        'Boil some water',
        'Steep tea in boiling water',
        'Pour tea in cup',
        'Add lemon',
    ])

    real_steps = main.make_tea()

    self.assertEqual(real_steps, expected_steps)
