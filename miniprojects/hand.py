#from cards import Card
from deck import Deck

class Hand(Deck):
    '''Hand Class'''

    def __init__(self, label=""):
        self.cards = []
        self.label = label



hand = Hand('new hand')
print(hand.cards)
print(hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)

my_hand = Hand('my_hand')
deck.move_cards(my_hand, 5)
print(my_hand)



