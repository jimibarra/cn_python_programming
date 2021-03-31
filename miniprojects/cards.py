class Card:
    ''' Card Class'''

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

card1 = Card(1,5)
card2 = Card(2,4)
card3 = Card(1,6)
card4 = Card(0,1)
card5 = Card(1,4)
#print(card1)
#print(card1 < card2)
#print(card1 < card3)
#print(card1 < card4)
#print(card1 < card5)





