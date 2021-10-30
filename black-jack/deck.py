from hand import Hand
from cards import Card
from random import shuffle

class Deck(Hand):
    def __init__(self):
        self.cards = [Card(j ,i) for j in range(1, 14) for i in range(4)]
        shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать:",
                          " карты закончились!")