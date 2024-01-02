import pandas as pd
import random

deck = []

# Suits are hearts (h), diamond (d), clubs (c), spades (s)
suits = ['h', 'd', 'c', 's']

# Creates list of numbered cards ranging from 2 thru 10
num_cards = [num for num in range(2, 11)]

# List of face cards
face_cards = ['J', 'Q', 'K', 'A']

# List of base card options with no assigned suit
base_cards = num_cards + face_cards

def create_deck():

    for card in base_cards:
        for suit in suits:
            deck.append(str(card)+suit)
        
    return deck

# print(deck)

file = open('deck_list.txt', 'w')
for item in deck:
    file.write(item+"\n")
file.close()