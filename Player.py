from Hand import *


class Player(Hand):
    """
    A player, their status and their cards
    """
    def __init__(self, name = ''):
        self.credits = 10                       # could be any start amount
        self.name = name
        self.cards = []                         # a players cards
        self.total = 0                          # store running hand total
        self.aces = 0 
                                  # flag for ace as 1 or 11
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