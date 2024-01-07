import random

class Deal:

    chosen_cards = []

    def __init__(self):
        self.first_card = self.choice()
        self.second_card = self.choice()
        self.hand = [self.first_card, self.second_card]


    # def deal(self):
    # self.card_one = choice()
    # second_card = choice()
    # hand = [first_card, second_card]
    #     return hand

    def choice():
    card = random.choice(deck)
    while card in chosen_cards: 
        card = random.choice(deck)
    chosen_cards.append(card)
    return card