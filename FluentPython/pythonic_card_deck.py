import collections

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


