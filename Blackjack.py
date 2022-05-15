# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:26:20 2022

@Authors: 
Mark D. Yarnell - 
Rabdaa -
Ollie KB -
@ A. Mcnulty - https://github.com/niall-anthony-mcnulty
"""

from Players import *
from CardDeck import Deck
from functions import *

if __name__ == "__main__":
    p1 = Player(input("Name: "))
    dealer = Dealer()

    while p1.credits > 0: 
        deck = Deck()                       # a new deck every hand
        deck.shuffle_fy()                      # shuffled
        p1.reset()
        dealer.reset()

        deal_hand(p1, dealer, deck)

        player_turn(p1, dealer, deck)       # to do - add more players, betting
        if not p1.bust:
            computer_turn(p1, dealer, deck)
        display_winner(p1, dealer)

    print(f"Sorry, {p1.name} you're out of credit!")
 