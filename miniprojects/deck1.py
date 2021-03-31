from cards import Card
import random

class Deck:
    '''Deck Class'''

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, size):
        hand_list = []
        count = 0
        for h in range(num_hands):
            count += 1
            hand = Hand('hand' + str(count))
            self.move_cards(hand, size)
            hand_list.append(hand)
        return hand_list

class Hand:
    '''Hand Class'''

    def __init__(self, label=""):
        self.cards = []
        self.label = label


deck = Deck()
t_hand = deck.deal_hands(3, 5)
print(t_hand)
