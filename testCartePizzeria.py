import unittest
from unittest.mock import patch, MagicMock
from cartePizzeria import CartePizzeria

class testCartePizzeria(unittest.TestCase):
    
    def setUp(self):
        self.carte = CartePizzeria()
    
    
    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty)
    
    def test_nb_pizzas(self):
        pizza_mock = MagicMock()
        self.carte.menu.append(pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)
    
    def test_add_pizza(self):
        pizza_mock = MagicMock()
        self.carte.add_pizza(pizza_mock)
        self.assertEqual(len(self.carte.menu), 1)
    
    def test_remove_pizza(self):
        pizza_mock = MagicMock()
        pizza_mock.name = "Pizza"
        self.carte.menu.append(pizza_mock)
        
        self.carte.remove_pizza("Pizza")
        self.assertEqual(len(self.carte.menu), 0)
        
if __name__ == '__main__':
    unittest.main()