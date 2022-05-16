

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
        self.bust = False

    def twist(self, card):  # add a card to the hand
        self.cards.append(card)  # add to hand
        if card.value > 10:  # court cards have indices 11 -13
            self.total += 10  # ... but value is 10
        else:
            self.total += card.value  # others have index = value
        if card.value == 1:  # except aces
            self.aces = True  # set flag

    def score(self):  # show the total
        return f'{self.total} {"or " + str(self.total + 10) if self.aces and self.total + 10 <= 21 else ""}'

    def best_score(self):
        """Returns best score possible accounting for aces"""
        if self.aces and self.total + 10 <= 21:  # one ace can count as  1 or 11 (others must be 1)
            return self.total + 10
        else:
            return self.total

    def get_hand(self):
        hand = ''
        for card in self.cards:
            hand += card.face()
            hand += ' '
        return hand

    def reset(self):  # reset for new hand
        self.total = 0
        self.cards = []
        self.aces = False
        self.bust = False


class Dealer(Player):
    """Represents the dealer (computer) inherits methods from Player"""

    def __init__(self, name=''):
        super().__init__()
        self.name = 'Dealer'
        self.credits = 10  # Adjust this value to get a better chance of winning
        self.turn = False

    def reset(self):  # reset for new hand
        super().reset()
        self.turn = False

    def show_hand(self):  # print list of cards
        if not self.turn:
            print('?')
            print(self.cards[1])  # Hide one card show the other
        else:
            for card in self.cards:
                print(card)

    def get_hand(self):
        hand = ''
        if not self.turn:
            hand = '? ' + self.cards[1].face()  # Hide one card show the other
        else:
            for card in self.cards:
                hand += card.face()
                hand += ' '
        return hand

    def score(self):  # show the total
        """Displays the computer score,
        Displays a question mark when it is the player's go and only one dealer card has been revealed"""
        if self.turn:
            return f'{self.total} {"or " + str(self.total + 10) if self.aces and self.total + 10 <= 21 else ""}'
        else:
            return '?'
