class Hand:
    """ Рука: набор карт на руках у одного игрока """
    
    def __init__(self):
        self.cards = []

    def clear(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.cards.append(card)
    
    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += f'{str(card)}\t'
        else:
            rep = "<пусто>"
        return rep