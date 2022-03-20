import errors
import unittest
import pizza_recipes
import pizza_stores
import pytest
from parameterized import parameterized, parameterized_class


class TestPizzaStore(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self.store = pizza_stores.SimplePizzaStore()

  @parameterized.expand([
    ('cheese',  pizza_recipes.CheezePizza),
    ('greek', pizza_recipes.GreekPizza),
    ('pepper', pizza_recipes.PepperoniPizza),
    ('veg', pizza_recipes.VeggiePizza),
  ])
  def test_create_pizza(self, pizza_name, pizza_clz):
    pizza_object = self.store.order_pizza(pizza_name)
    self.assertTrue(isinstance(pizza_object, pizza_clz))

  def test_unknown_pizza(self):
    with pytest.raises(errors.UnknownPizzaNameError) as e_info:
      self.store.order_pizza('unknown_pizza')
