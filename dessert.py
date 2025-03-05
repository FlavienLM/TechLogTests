from menuElement import MenuElement

class Dessert(MenuElement):
    def __init__(self, name:str, prix:float, ingredients, homemade:bool):
        super().__init__(name,prix)
        self.ingredients = ingredients
        self.homemade = homemade