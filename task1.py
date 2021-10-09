class Soda():
    """Газированная вода"""
    def __init__(self, addit):
        if isinstance(addit, str):
            self.addit = addit
        else:
            self.addit

    def show_my_drink(self):
        if self.addit:
            print(f'Газировка и {self.addit}')
        else:
            print("Обычная газировка")