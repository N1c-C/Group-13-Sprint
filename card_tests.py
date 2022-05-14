# Tests to demonstrate Card related classes


from Cards import Deck

card_deck = Deck()


def display_deck(deck):
    for i in range(deck.count()):
        card = deck.deal()
        print(f'{card} ', end='')


# Check there are 52 cards, deal and display cards:
print(f'Cards in pack: {card_deck.count()}')
display_deck(card_deck)

# Shuffle the pack then display cards
card_deck = Deck()
card_deck.shuffle()

print('\n\nCard order after a random shuffle')
display_deck(card_deck)

# For fun:shuffle the pack using fisher-yates algorithm

card_deck = Deck()
card_deck.shuffle_fy()

print('\n\nCard order after Fisher-Yates shuffle')
display_deck(card_deck)
