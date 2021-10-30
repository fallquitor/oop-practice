import cards, game, deck, hand

from random import shuffle

class BJ_Card(cards.Positionable_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            return self.rank if self.rank <= 10 else 10
        else:
            return None

class BJ_Deck(deck.Deck):
    def __init__(self):
        self.cards = [BJ_Card(j ,i) for j in range(1, 14) for i in range(4)]
        shuffle(self.cards)

class BJ_Hand(hand.Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def total(self):
        if None in [i.value for i in self.cards]:
            return None
        t = sum([i.value for i in self.cards])
        if 1 in [i.value for i in self.cards] and t <= 11:
            t += 10
        return t

    @property
    def is_busted(self):
        return self.total > 21

    def __str__(self):
        return f"{self.name}:\t{super().__str__()} ( {self.total} )"

class BJ_Player(BJ_Hand):
    def __init__(self, name, bank, dealer):
        super().__init__(name)
        self.bank = bank
        self.bid = None
        self.dealer = dealer

    def is_hitting(self):
        return game.ask_yes_no(f"\n{self.name}, будете брать ещё карты?")

    def win(self):
        self.bank += self.bid
        self.dealer.bank -= self.bid
        self.bid = None
        print(f"{self.name} выиграл(а).")
    
    def lose(self):
        self.bank -= self.bid
        self.dealer.bank += self.bid
        self.bid = None
        print(f"{self.name} проиграл(а).")
        

    def push(self):
        self.bid = None
        print(f"{self.name} сыграл(а) с дилером в ничью.")

    def bust(self):
        print(f"{self.name} перебрал(а).")
        self.lose()

class BJ_Dealer(BJ_Hand):
    def __init__(self):
        super().__init__("Дилер")

        self.bank = 300

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(f"{self.name} перебрал(а).")

    def flip_first_card(self):
        self.cards[0].flip()

class BJ_Game:
    def __init__(self, names, banks):
        self.dealer = BJ_Dealer()

        self.players = [BJ_Player(i, j, self.dealer) for i, j in zip(names, banks)]

        self.deck = BJ_Deck()
    
    @property
    def still_playing(self):
        sp = []
        for i in self.players:
            if not i.is_busted:
                sp.append(i)
        return sp
    
    def __additional_cards(self, player):
        if len(self.deck.cards) < 2:
            self.deck = BJ_Deck()
        while not player.is_busted and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted:
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()

        for i in self.players:
            print(f"Банк игрока {i.name} : {i.bank}")

        print(f"\nДеньги казино : {self.dealer.bank}")

        for i in self.players:
            i.bid = game.ask_num(f"Какая ставка у игрока {i.name} : ", l=1, h=i.bank + 1)

        for i in self.players:
            print(i)
        print(self.dealer)

        for i in self.players:
            self.__additional_cards(i)

        self.dealer.flip_first_card()

        print(self.dealer)
        if self.still_playing:
            self.__additional_cards(self.dealer)

        if self.dealer.is_busted:
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

        new_players = []

        for i in self.players:
            if i.bank <= 0:
                print(f"{i.name} проиграл всё в казино. Кто-то дайте ему денег у него же 3 ребёнка. Грустная история.")
            else:
                new_players.append(i)
        
        self.players = new_players

        if len(self.players) <= 0:
            print("Игра в покер с таким кол-вом людей невозможно. Игра оконченна.")
            exit()

def main():
    print("\t\tДобро пожаловать в игру Блек-джек!\n")
    names = []
    banks = []
    number = game.ask_num("Сколько всего игроков?(1 - 7): ", 1, 8)

    for i in range(number):
        name = input(f"Введите имя игрока № {i+1} : ")
        bank = game.ask_num(f"Введите банк игрока № {i+1} : ")
        names.append(name)
        banks.append(bank)
    print()

    _game = BJ_Game(names, banks)

    again = True
    while again:
        if len(_game.deck.cards) < (len(names) + 1) * 2:
            _game.deck = BJ_Deck()
        _game.play()
        again = game.ask_yes_no("\n Хотите сыграть ещё раз?")


if __name__ == "__main__":
    main()