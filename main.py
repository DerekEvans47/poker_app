# TODO: Create deck
# TODO: Create class for n number of CPU players
# TODO: Create a class instead of definitions/functions
# TODO: Find way to add number of hand integer to the CPU hand
# TODO: Create way to deal deck
# TODO: Add logic for CPU hands to not include player chosen cards
# TODO: Create way for user to obtain cards
# TODO: Create way for hand evaluation
# TODO: Need to implement hand combinations (based on what player has)
    # If the user has "A" if they get the same ("A") is 1 pair, if they get "A" (SAME CARD) (THREE OTHER SAME CARDS) - full house
    # Does it make sense that one pair x2 is two pair?
# TODO: Create user choice for what happens next
# TODO: Try to put the context of development and application in terms of user stories, features, and epics

# EPIC - Poker Application
# FEATURE - Hand Evaluation
# STORY - As a user I want to be able to verify my hands viability

import pandas as pd
import random
from deck import create_deck

deck = create_deck()
chosen_cards = []
known_cards = []
remaining_deck = []
players_starting_hand = []


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
    player_first = input("What hand do you want to test?\nPlease enter your first card: ")
    player_second = input("Please enter your second card: ")
    players_starting_hand.append(player_first)
    players_starting_hand.append(player_second)
    chosen_cards.append(player_first)
    chosen_cards.append(player_second)
    known_cards.append(player_first)
    known_cards.append(player_second)
    remaining_deck_cards(known_cards)
    return players_starting_hand

def remaining_deck_cards(known_cards):
    for card in deck:
        if card not in known_cards:
            remaining_deck.append(card)
    return remaining_deck

def community_deal():
    community_cards = []
    cards_left = 5
    while cards_left > 0:
        community_card = choice()
        community_cards.append(community_card)
        cards_left -= 1
    print(community_cards)
    return community_cards

# players_hand, known_cards = player_hand()
# print(players_hand)

number_players = 7

for players in range(0, number_players):
    hand_num = deal()
    print(deal())

community_deal()