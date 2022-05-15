from Cards import *
from Deck import *

class Hand(Deck):
    """"a hand of cards. Either player or dealer"""
    def __init__(self):
        self.cards = []                         # initially no cards dealt