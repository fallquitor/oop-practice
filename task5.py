class Tomato:
    STATES = ["None", "Flower", "Green tomato", "Red tomato"]

    def __init__(self, index):
        self.__index = index
        self.__state = 0

    def grow(self):
        if self.__state < 3:
            self.__state += 1

    @property
    def is_ripe(self):
        return self.__state >= 3

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    @property
    def all_are_ripe(self):
        return False not in [i.is_ripe for i in self.tomatoes]

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.__plant = plant

    def work(self):
        print("Gardener is working")
        self.__plant.grow_all()

    def harvest(self):
        print("Gardener is picking up")
        if self.__plant.all_are_ripe:
            self.__plant.give_away_all()
            print("He picked up everything")
        else:
            print("Not all the tomatoes growed")

    @staticmethod
    def knowledge_base():
        print("""
1. Plant
2. Wait
3. Collect
4. Wait if not every tomato growed
5. Repeat
"""
)

def main():
    Gardener.knowledge_base()
    tom = TomatoBush(3)
    gar = Gardener("Artem", tom)
    gar.work()
    gar.harvest()
    while not tom.all_are_ripe:
        gar.work()
    gar.harvest()
if __name__ == "__main__":
    main()