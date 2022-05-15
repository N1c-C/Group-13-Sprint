# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:26:20 2022

@Authors: 
Mark D. Yarnell - 
Mark -
Olli -
@ A. Mcnulty - https://github.com/niall-anthony-mcnulty
"""
import random  # needed for shuffling
from Cards import *
from Dealer import *
from Hand import *
from Player import *
from Deck import *
from functions import *

if __name__ == "__main__":  
    
    
  
    p1 = Player(input("Name: "))
    dealer = Dealer()

    while p1.credits > 0: 
        deck = Deck()                           # a new deck every hand
        deck.shuffle()                      # shuffled
        play_hand(p1, dealer)               # to do - add more players, betting
    print("Sorry, you're out of credit!")
 