# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:13:01 2022

@author: Mark D. Yarnell
"""


def play_hand(player, dealer):
    """
    player : a member of Player Class
    dealer : a special member of Player Class
    """
    player.reset()                          # reset variables
    player.deal()                           # first 2 cards
    player.print_score()   
    while player.total <= 21:               # still in play
        decision = input("0 = STICK, 1 = TWIST ")
        if decision == "1":                 
            player.twist()                  # 1 more card
            player.print_score()
        else:
            break
    if player.total > 21:                   # dealer auto wins
        player.lost()
        return
    if player.aces > 0 and player.total <= 11:
        player.total += 10                  # score an ace as 11
    dealer.reset()
    dealer.deal()
    dealer.print_score()
    """" awkward condition to account for various scenarios incl aces"""
    while dealer.total < player.total and dealer.total + 10*dealer.aces > 21 or dealer.total + 10*dealer.aces < player.total:
        dealer.twist()
        dealer.print_score()
    if dealer.total <= 21 and dealer.total >= player.total:
        player.lost()
    else:
        player.won() 
    new_hand()
def new_hand():                             # leave a gap between hands
    print("---")
    print()

""" The main function is very simple """

p1 = Player(input("Name: "))
dealer = Player("Dealer")

while p1.credits > 0: 
    deck = Deck()                       # a new deck every hand
    deck.shuffle()                      # shuffled
    play_hand(p1, dealer)               # to do - add more players, betting
print("Sorry, you're out of credit!")  
