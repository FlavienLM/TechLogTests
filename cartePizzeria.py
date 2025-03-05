from pizza import Pizza
from cartePizzeriaException import CartePizzeriaException
class CartePizzeria:
    
    def __init__(self):
        self.menu = []
    
    def is_empty(self):
        return len(self.menu) == 0
    
    def nb_pizzas(self):
        return len(self.menu)
    
    def add_pizza(self, pizza: Pizza):
        self.menu.append(pizza)
        
    def remove_pizza(self, name: str):
        for i in range (self.nb_pizzas()):
            if self.menu[i].name == name:
                self.menu.pop(i)
                return
        return CartePizzeriaException()