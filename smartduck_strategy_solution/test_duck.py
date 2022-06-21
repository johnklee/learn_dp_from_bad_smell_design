"""Unit test cases of duck module."""

import unittest
import duck


class TestDuck(unittest.TestCase):

  def setUp(self):
    super().setUp()

  def test_duck(self):
    duck_obj = duck.Duck()
    self.assertEqual(duck_obj.quack(), 'quack!')
    self.assertEqual(duck_obj.display(), 'I am a duck!')
    self.assertEqual(duck_obj.swim(), 'I can swim!')
    # self.assertEqual(duck_obj.fly(), 'I can fly!')

  def test_mallard_duck(self):
    duck_obj = duck.MallardDuck()
    self.assertEqual(duck_obj.quack(), 'quack!')
    self.assertEqual(duck_obj.display(), 'I am a mallard duck ^^')
    self.assertEqual(duck_obj.swim(), 'I can swim!')
    # self.assertEqual(duck_obj.swim(), 'I can fly!')

  def test_redhead_duck(self):
    duck_obj = duck.RedheadDuck()
    self.assertEqual(duck_obj.quack(), 'quack!')
    self.assertEqual(duck_obj.display(), 'I am a redhead duck @_@')
    self.assertEqual(duck_obj.swim(), 'I can swim!')
    # self.assertEqual(duck_obj.swim(), 'I can fly!')

  def test_redhead_duck(self):
    duck_obj = duck.RubberDuck()
    self.assertEqual(duck_obj.quack(), 'squeak!')
    self.assertEqual(duck_obj.display(), 'I am a rubber duck ><"')
    self.assertEqual(duck_obj.swim(), 'I can swim!')
    # self.assertEqual(duck_obj.swim(), 'I can not fly!')
