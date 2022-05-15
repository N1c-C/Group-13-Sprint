from Dealer import *

# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:09:15 2022

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




# def computer_player_hand():
#     #When this function is called, the dealer's score is reset for another round, a credit is paid, the dealer's turn is
#     #taken and the process is displayed as text. The dealer's score remains 
#     dealer.reset() #resets the score
#     if dealer.credits == 0:
#         print("Congratulations! The dealer ran out of credits! You won!")
#         # game_complete()
#     dealer.credits -= 1
#     print("Dealer's turn... Dealer paid 1 credit to play. Dealer currently has ", dealer.credits, " credits.")
#     while dealer.total < 22:
#         if 15 < dealer.total < 22:
#             print("Dealer has chosen to STICK with", dealer.total)
#             break
#         print("Dealer takes a card...")
#         time.sleep(2)
#         card = deck.deal()
#         print("Dealer drew ", card.value)
#         time.sleep(2)
#         dealer.total += card.value
#         print("Dealer's total is currently ", dealer.total)
#         time.sleep(2)
#     if dealer.total > 21:
#         print("Dealer went bust! Dealer scored 0. Your turn!")
#         dealer.reset()
    # play_hand() 