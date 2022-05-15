"""
Card Classes for Group 13 Sprint
"""

class Card:
    """ Represents a single playing card
    param: suit (str) H,D,C or S: On instantiation assigned to self.suit
    param: value (int) 1-13: On instantiation assigned to self.value
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.display = str(self.suit) + " " + str(self.value)

    def __repr__(self):
        return str(self)

    def __str__(self):
        """Convert the values to standard card format as a str"""
        vals = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return vals[self.value] + self.suit   

    
    