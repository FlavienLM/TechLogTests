import unittest
from unittest.mock import patch, MagicMock
from cartePizzeria import CartePizzeria
from dessert import Dessert
from drinks import Drinks
from pizza import Pizza


class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty)

    def test_nb_pizzas(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock2 = MagicMock(spec=Pizza)
        drinks_mock1 = MagicMock(spec=Drinks)
        dessert_mock1 = MagicMock(spec=Dessert)
        dessert_mock2 = MagicMock(spec=Dessert)
        dessert_mock3 = MagicMock(spec=Dessert)
        self.carte.menu.append(pizza_mock1)
        self.carte.menu.append(pizza_mock2)
        self.carte.menu.append(drinks_mock1)
        self.carte.menu.append(dessert_mock1)
        self.carte.menu.append(dessert_mock2)
        self.carte.menu.append(dessert_mock3)
        self.assertEqual(self.carte.nb_pizzas(), 2)

    def test_nb_drinks(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock2 = MagicMock(spec=Pizza)
        drinks_mock1 = MagicMock(spec=Drinks)
        dessert_mock1 = MagicMock(spec=Dessert)
        dessert_mock2 = MagicMock(spec=Dessert)
        dessert_mock3 = MagicMock(spec=Dessert)
        self.carte.menu.append(pizza_mock1)
        self.carte.menu.append(pizza_mock2)
        self.carte.menu.append(drinks_mock1)
        self.carte.menu.append(dessert_mock1)
        self.carte.menu.append(dessert_mock2)
        self.carte.menu.append(dessert_mock3)
        self.assertEqual(self.carte.nb_drinks(), 1)

    def test_nb_desserts(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock2 = MagicMock(spec=Pizza)
        drinks_mock1 = MagicMock(spec=Drinks)
        dessert_mock1 = MagicMock(spec=Dessert)
        dessert_mock2 = MagicMock(spec=Dessert)
        dessert_mock3 = MagicMock(spec=Dessert)
        self.carte.menu.append(pizza_mock1)
        self.carte.menu.append(pizza_mock2)
        self.carte.menu.append(drinks_mock1)
        self.carte.menu.append(dessert_mock1)
        self.carte.menu.append(dessert_mock2)
        self.carte.menu.append(dessert_mock3)
        self.assertEqual(self.carte.nb_dessert(), 3)

    def test_add_drink_identique(self):
        drink_mock1 = MagicMock(spec=Drinks)
        drink_mock1.name = "Boisson"
        drink_mock2 = MagicMock(spec=Drinks)
        drink_mock2.name = "Boisson"
        self.carte.add(drink_mock1)
        self.carte.add(drink_mock2)
        self.assertEqual(len(self.carte.menu), 1)

    def test_add_drink_non_identique(self):
        drink_mock1 = MagicMock(spec=Drinks)
        drink_mock1.name = "Boisson"
        drink_mock2 = MagicMock(spec=Drinks)
        drink_mock2.name = "Boisson machiavélique"
        self.carte.add(drink_mock1)
        self.carte.add(drink_mock2)
        self.assertEqual(len(self.carte.menu), 2)

    def test_add_dessert_identique(self):
        dessert_mock1 = MagicMock(spec=Dessert)
        dessert_mock1.name = "Déssert"
        dessert_mock2 = MagicMock(spec=Dessert)
        dessert_mock2.name = "Déssert"
        self.carte.add(dessert_mock1)
        self.carte.add(dessert_mock2)
        self.assertEqual(len(self.carte.menu), 1)

    def test_add_dessert_non_identique(self):
        dessert_mock1 = MagicMock(spec=Dessert)
        dessert_mock1.name = "Déssert"
        dessert_mock2 = MagicMock(spec=Dessert)
        dessert_mock2.name = "Déssert machiavélique"
        self.carte.add(dessert_mock1)
        self.carte.add(dessert_mock2)
        self.assertEqual(len(self.carte.menu), 2)

    def test_add_pizza_identique(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock1.name = "Pizza"
        pizza_mock1.ingredients = ["Jambom", "Fromage"]
        pizza_mock1.base = "Tomate"
        pizza_mock2 = MagicMock(spec=Pizza)
        pizza_mock2.name = "Pizza"
        pizza_mock2.ingredients = ["Jambom", "Fromage"]
        pizza_mock2.base = "Tomate"

        self.carte.add(pizza_mock1)
        self.carte.add(pizza_mock2)

        self.assertEqual(len(self.carte.menu), 1)

    def test_add_pizza_non_identique(self):
        pizza_mock1 = MagicMock(spec=Pizza)
        pizza_mock1.name = "Pizza"
        pizza_mock1.ingredients = ["Tomate", "Fromage"]
        pizza_mock1.base = "Tomate"
        pizza_mock2 = MagicMock(spec=Pizza)
        pizza_mock2.name = "Pizza"
        pizza_mock2.ingredients = ["Fraise", "Fromage"]
        pizza_mock2.base = "Tomate"

        self.carte.menu.append(pizza_mock1)
        self.carte.menu.append(pizza_mock2)

        self.assertEqual(len(self.carte.menu), 2)


if __name__ == '__main__':
    unittest.main()
