# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:26:20 2022
@author: Mark D. Yarnell
"""
import random  # needed for shuffling

class Card:
    """
    Represents card
    Display eg 5H for 5 of Hearts, TD for 10 of Diamonds
    """
    def __init__(self, suit = 0, value = 2):
        self.suit = suit
        self.value = value
        
    suit_names = ['C', 'D', 'H', 'S']
    value_names = [None, 'A', '2', '3', '4', '5', '6', '7', '8','9', 'T', 'J', 'Q', 'K']
    
    def __str__(self):
        return '%s%s' %(Card.value_names[self.value],
                            Card.suit_names[self.suit])
    
class Deck:
    """
    Deck represents the available cards in deck
    They are popped off when dealt
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):                   # loop suits
            for value in range(1, 14):           # loop value
                card = Card(suit, value) 
                self.cards.append(card)         # add this card to deck
    def pop_card(self):                         # deal card by popping off the top
        return self.cards.pop()
    def add_card(self, card):                   # add a card to hand/deck
        self.cards.append(card)
    def shuffle(self):                          # after each hand
        random.shuffle(self.cards)
        
class Hand(Deck):
    """"a hand of cards. Either player or dealer"""
    def __init__(self):
        self.cards = []                         # initially no cards dealt
        
class Player(Hand):
    """
    A player, their status and their cards
    """
    def __init__(self, name = ''):
        self.credits = 10                       # could be any start amount
        self.name = name
        self.cards = []                         # a players cards
        self.total = 0                          # store running hand total
        self.aces = 0                           # flag for ace as 1 or 11
    def deal(self):                             # initial 2 cards
        for i in range(2):
            card = deck.pop_card()              # deal off top of deck
            self.add_card(card)                 # add to hand
            if card.value > 10:                  # court cards have indices 11 -13
                self.total += 10                # ... but value is 10
            else:                               
                self.total += card.value         # others have index = value
            if card.value == 1:                  # except aces
                self.aces = 1                   # set flag
        Player.show_hand(self)
    def twist(self):                            # one card at a time
        card = deck.pop_card()                  
        self.add_card(card)                     
        if card.value > 10:
            self.total += 10
        else:
            self.total += card.value
        if card.value == 1:
            self.aces = 1
        Player.show_hand(self)
    def print_score(self):                      # show the total
        print("SCORE: ", self.total)
        if self.aces > 0:                       # ace can count 1 or 11
            print("or ", self.total + 10)
    def show_hand(self):                        # print list of cards
        for card in self.cards:
            print(card)
    def reset(self):                            # resetfor new hand
        self.total = 0
        self.cards = []
        self.aces = 0
    def won(self):                              # invoked when player wins
        self.credits += 1                       # could be a bet amount
        print("You WON! Credits = ", self.credits)
    def lost(self):                             # invoked when loses
        self.credits -= 1
        print("You LOST! Credits = ", self.credits)

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