from random import shuffle

class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"



class Deck:
    suits = ["hearts","diamonds","clubs","spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))
        # print(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full deck can shuffled")
        shuffle(self.cards)


    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


d = Deck()
# print(d)
# print(d.count())
# # print(d._deal(52))
# print(d.count())
# print(d._deal(2))
# # d.shuffle()
# print(d.cards)

card = d.deal_card()
print(card)

hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)


# c = Card("10", "clubs")
# print(c)


# Deck()   ----> simpli print list of Deck
# print(Deck())   ----> print list but show address of Deck object
# print(self.cards)   ----> error  NameError: name 'self' is not defined
