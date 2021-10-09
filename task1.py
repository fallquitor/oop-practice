class Soda():
    """Газированная вода"""
    def __init__(self, add = None):
        self.add = add

    def show_my_drink():
        if add != None:
            print("Газировка " + self.add)

soda = Soda(add = input("Что хотите добавить? "))