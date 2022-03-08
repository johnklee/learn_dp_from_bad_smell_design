import errors
import unittest
import taiwan_pizza_store
import taiwan_pizza_recipes
import pytest
from parameterized import parameterized, parameterized_class


class TestPizzaStore(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self.store = taiwan_pizza_store.TaiwanPizzaStore()

  @parameterized.expand([
    ('cheeze',  taiwan_pizza_recipes.TaiwanCheezePizza),
    ('greek', taiwan_pizza_recipes.TaiwanGreekPizza),
    ('pepper', taiwan_pizza_recipes.TaiwanPepperoniPizza),
    ('veg', taiwan_pizza_recipes.TaiwanVeggiePizza),
  ])
  def test_create_pizza(self, pizza_name, pizza_clz):
    pizza_object = self.store.order_pizza(pizza_name)
    self.assertTrue(isinstance(pizza_object, pizza_clz))

  def test_unknown_pizza(self):
    with pytest.raises(errors.UnknownPizzaNameError) as e_info:
      self.store.order_pizza('unknown_pizza')
