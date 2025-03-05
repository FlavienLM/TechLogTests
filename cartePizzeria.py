from pizza import Pizza
from drinks import Drinks
from dessert import Dessert
from cartePizzeriaException import CartePizzeriaException
from menuElement import MenuElement
class CartePizzeria:
    
    def __init__(self):
        self.menu = []
    
    def is_empty(self):
        return len(self.menu) == 0
    
    def nb_pizzas(self):
        res = 0
        for i in range(len(self.menu)):
            el = self.menu[i]
            if(isinstance(el, Pizza)):
                res+=1
        return res
    
    def nb_drinks(self):
        res = 0
        for i in range(len(self.menu)):
            el = self.menu[i]
            if(isinstance(el, Drinks)):
                res+=1
        return res
    
    def nb_dessert(self):
        res = 0
        for i in range(len(self.menu)):
            el = self.menu[i]
            if(isinstance(el, Dessert)):
                res+=1
        return res
    
    def identique(self,el1, el2):
        if(isinstance(el2, Pizza)):
            return el1.name == el2.name and el1.ingredients == el2.ingredients and el1.base == el2.base
        else:
            return el1.name == el2.name
    
    def add(self, element: MenuElement):
        class_element = element.__class__
        for i in range(len(self.menu)):
            el = self.menu[i]
            if(el.__class__ == class_element):
                if(self.identique(el,element)):
                    return
        self.menu.append(element)
        
    def remove(self, name: str):
        for i in range (len(self.menu)):
            if self.menu[i].name == name:
                self.menu.pop(i)
                return
        return CartePizzeriaException()