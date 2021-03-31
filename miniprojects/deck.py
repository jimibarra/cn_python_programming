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
            #hand.add_card(self.pop_card())
            hand.append(self.pop_card())
        return hand

    def deal_hands(self, num_hands, size):
        hands_list = []
        for h in range(num_hands):
            hand = []
            self.move_cards(hand, size)
            hands_list.append(hand)
        return hands_list

    def print_list(self, list):
        new_list = []
        for item in list:
            new_list.append(str(item))
        return new_list


deck = Deck()
deck.shuffle()

#my_hand = []
#deck.move_cards(my_hand,8)
#response = deck.print_list(my_hand)
#print(response)

my_list = deck.deal_hands(5, 7)
for hand in my_list:
    response = deck.print_list(hand)
    print(response)












#print(deck)
#deal = deck.pop_card()
#print(deal)
#deal = deck.pop_card()
#print(deal)

#tcard = Card(1,10)
#print(tcard)

#deck.add_card(tcard)
#print(deck)

#deck.shuffle()
#print(deck)

#deck.sort()
#print(deck)




