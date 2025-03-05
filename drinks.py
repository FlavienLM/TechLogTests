from menuElement import MenuElement


class Drinks(MenuElement):

    def __init__(self, name: str, prix: float, alcohol: bool):
        super().__init__(name, prix)
        self.alcohol = alcohol
