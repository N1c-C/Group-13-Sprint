"""
Card Classes for Group 13 Sprint
"""
import random


class Card:
    """ Represents a single playing card
    param: suit (str) H,D,C or S: On instantiation assigned to self.suit
    param: value (int) 1-13: On instantiation assigned to self.value
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.display = str(self.suit) + " " + str(self.value)
        self.vals = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __str__(self):
        """for printing if needed"""
        self.face()

    def face(self):
        """Returns the face (value and suit) of a card"""
        return self.vals[self.value] + self.suit


class Deck:
    """
    Deck represents the available cards in deck
    They are popped off when dealt
    """

    def __init__(self):
        self.cards = []
        for suit in ['H', 'D', 'S', 'C']:  # loop suits
            for value in range(1, 14):  # loop value
                self.cards.append(Card(suit, value))  # add this card to deck

    def deal(self):
        """ Removes and returns the first Card object in the self._deck list"""
        return self.cards.pop(0)

    def add_card(self, card):  # add a card to hand
        self.cards.append(card)

    def shuffle(self):  # after each hand
        random.shuffle(self.cards)

    def count(self):
        """Returns the number of Cards objects in self._deck"""
        return len(self.cards)

    def shuffle_fy(self):
        """ Shuffles the deck using the Fisher-Yates shuffling algorithm.
        A randomly selected kth card is swapped with the nth card
        param: n decremental index of all Card objects in current deck
        param: k random Card Selection"""

        for n in range(self.count() - 1, -1, -1):
            k = random.randint(0, n)
            self.cards[k], self.cards[n] = self.cards[n], self.cards[k]