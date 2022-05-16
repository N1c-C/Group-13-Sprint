

class Player:
    """
    A player, their status and their cards
    """

    def __init__(self, name=''):
        self.credits = 10  # could be any start amount
        self.name = name
        self.cards = []  # a players cards
        self.total = 0  # store running hand total
        self.aces = False  # flag for ace as 1 or 11
        self.bust = False  # Flag set when bust to avoid dealer's go

    def twist(self, card):
        """Receives a card from the deck and appends it to the players hand
        updates the players score and aces flag as necessary
        param: card: Card object"""
        self.cards.append(card)  # add to hand
        if card.value > 10:  # court cards have indices 11 -13
            self.total += 10  # ... but value is 10
        else:
            self.total += card.value  # others have index = value
        if card.value == 1:  # except aces
            self.aces = True  # set flag

    def score(self):
        """Returns formatted string of current total. Allowing for totals with aces when required """
        return f'{self.total} {"or " + str(self.total + 10) if self.aces and self.total + 10 <= 21 else ""}'

    def best_score(self):
        """Returns best score possible accounting for aces as an int"""
        if self.aces and self.total + 10 <= 21:  # one ace can count as  1 or 11 (others must be 1)
            return self.total + 10
        else:
            return self.total

    def get_hand(self):
        """Returns the hand as a string so that it can be displayed by the UI"""
        hand = ''
        for card in self.cards:
            hand += card.face()
            hand += ' '
        return hand

    def reset(self):
        """Resets the player for the next go"""
        self.total = 0
        self.cards = []
        self.aces = False
        self.bust = False


class Dealer(Player):
    """Represents the dealer (computer) inherits methods from Player
    Overloads methods as required """

    def __init__(self, name=''):
        super().__init__()
        self.name = 'Dealer'
        self.credits = 10  # Adjust this value to get a better chance of winning
        self.turn = False  # Flag: So the dealer's first card and score remain hidden until it is the dealers turn

    def reset(self):  # reset for new hand
        super().reset()
        self.turn = False

    def get_hand(self):
        """Returns the hand as a string so that it can be displayed by the UI
        Takes into account if it is the deals turn or not.
        If self.turn is False represents the first card as a ?"""
        hand = ''
        if not self.turn:
            hand = '? ' + self.cards[1].face()  # Hide one card show the other
        else:
            for card in self.cards:
                hand += card.face()
                hand += ' '
        return hand

    def score(self):  # show the total
        """Returns the computer score as a formatted str.
        Returns a question mark when it is the player's go and only one dealer card has been revealed"""
        if self.turn:
            return f'{self.total} {"or " + str(self.total + 10) if self.aces and self.total + 10 <= 21 else ""}'
        else:
            return '?'
