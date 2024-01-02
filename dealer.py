import pandas as pd
import random
from deck import create_deck

deck = create_deck()
chosen_cards = []
known_cards = []


def choice():
    
    card = random.choice(deck)

    while card in chosen_cards: 
        card = random.choice(deck)
    chosen_cards.append(card)
    return card

def deal():
    first_card = choice()
    second_card = choice()
    hand = [first_card, second_card]

    return hand

def player_hand():

    player_first = [input("What hand do you want to test?\nPlease enter your first card: ")] 
    player_second = [input("Please enter your second card: ")]
    player_hand = player_first + player_second
    chosen_cards.append(player_hand)
    known_cards.append(player_hand)

    return player_hand

def remaining_deck_cards(known_cards = known_cards):
    remaining_deck_cards = [deck not in known_cards]
    print(remaining_deck_cards)
    return remaining_deck_cards