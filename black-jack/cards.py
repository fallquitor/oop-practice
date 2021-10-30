class Card:
    """ 
        Одна игральная карта 

        0 - ♠

        1 - ♣

        2 - ♥

        3 - ♦
    """
    
    RANKS = ["Т", "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "K"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666'] 

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return Card.RANKS[self.rank - 1] + Card.SUITS[self.suit]

class Unprintable_Card(Card):
    """ Карта, номинал и масть которой 
    не могут быть выведены на экран. """
    
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """ Карта, которую можно положить 
    лицом или рубашкой вверх. """
    
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def flip(self):
        self.is_face_up = not self.is_face_up

    def __str__(self):
        if self.is_face_up:
            return super().__str__()
        else:
            return "XX"