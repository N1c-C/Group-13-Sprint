# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:08:59 2022

@author: Mark D. yarnell
"""


p1 = Player(input("Name: "))
dealer = Player("Dealer")

while p1.credits > 0: 
    deck = Deck()                       # a new deck every hand
    deck.shuffle()                      # shuffled
    play_hand(p1, dealer)               # to do - add more players, betting
print("Sorry, you're out of credit!")  
