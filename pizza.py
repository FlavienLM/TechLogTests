from menuElement import MenuElement


class Pizza(MenuElement):

    def __init__(self, name: str, 
                prix: float, 
                ingredients, 
                description: str, 
                base: str):
        super().__init__(name, prix)
        self.ingredients = ingredients
        self.description = description
        self.base = base
