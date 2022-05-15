from Cards import Card
import random

class Deck:
    """
    Deck represents the available cards in deck
    They are popped off when dealt
    """
    def __init__(self):
        self.cards = []
        for suit in ['H', 'D', 'S', 'C']:        # loop suits
            for value in range(1, 14):           # loop value
                self.cards.append(Card(suit, value))      # add this card to deck
    
    def __str__(self):
        for card_obj in self.cards:
            return(str(self.cards))

    def __repr__(self):
        return str(self)

    def pop_card(self):                         # deal card by popping off the top
        return self.cards.pop()
    
    def deal(self):
        """ Removes and returns the first Card object in the self._deck list"""
        return self.cards.pop(0)

    def add_card(self,card):                   # add a card to hand
        self.cards.append(card)
    
    def shuffle(self):                          # after each hand
        random.shuffle(self.cards)
    
    def count(self):
        """Returns the number of Cards objects in self._deck"""
        return len(self.cards)

    def shuffle_fy(self):
        """ Shuffles the deck using the Fisher-Yates shuffling algorithm.
        A randomly selected kth card is swapped with the nth card
        param: n decremental index of all Card objects in current deck
        param: k random Card Selection"""

        for n in range(self.count()-1, -1, -1):
            k = random.randint(0, n)
            self.cards[k], self.cards[n] = self.cards[n], self.cards[k]