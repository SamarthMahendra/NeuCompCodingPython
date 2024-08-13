import collections
from random import choice

# named tuple card - rank, suit

Card = collections.namedtuple('card',['rank', 'suit'])

class FrenchDeck:

    ranks = [
        i for i in range(2,11)
    ] + list('JKQA')
    suits = "Spades Diamonds Clubs Hearts".split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for rank in self.ranks
            for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]




# testing
deck = FrenchDeck()
print(len(deck))
print(deck[10])

# random
print(choice(deck))

# slicing
print(deck[10:12])
print(deck[:2])


# iterable
for card in deck:
    print(card)

print("Reversed")

# iterate reverse
for card in reversed(deck):
    print(card)

print('\n')
print("contains:")

# contains
print(Card(rank='A', suit='Hearts') in deck)
print(Card(rank='X', suit='Hearts') in deck)


# sorting
print("sorting")
suit_values = dict(Spades=3, Hearts=2, Diamonds=1, Clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)



