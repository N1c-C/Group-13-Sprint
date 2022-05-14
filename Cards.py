"""
Card Classes for Group 13 Sprint
"""

import random


class Card:
    """ Represents a single playing card
    param: suit (str) H,D,C or S: On instantiation assigned to self.suit
    param: value (int) 1-13: On instantiation assigned to self.value"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        """Convert the values to standard card format as a str"""
        vals = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return vals[self.value] + self.suit    

class Deck:
    """ Represents a pack of 52 Card objects
     On instantiation 52 Card objets are added to the internal _deck list
     param: self._deck: List holding the current Card objects in the Deck"""

    def __init__(self):
        self._deck = []
        for suit in ['H', 'D', 'S', 'C']:
            for value in range(1, 14):
                self._deck.append(Card(suit, value))

    def shuffle(self):
        """Randomly shuffles self._deck"""
        random.shuffle(self._deck)

    def deal(self):
        """ Removes and returns the first Card object in the self._deck list"""
        return self._deck.pop(0)

    def count(self):
        """Returns the number of Cards objects in self._deck"""
        return len(self._deck)

    def shuffle_fy(self):
        """ Shuffles the deck using the Fisher-Yates shuffling algorithm.
        A randomly selected kth card is swapped with the nth card
        param: n decremental index of all Card objects in current deck
        param: k random Card Selection"""

        for n in range(self.count()-1, -1, -1):
            k = random.randint(0, n)
            self._deck[k], self._deck[n] = self._deck[n], self._deck[k]
