# -*- coding: utf-8 -*-

from time import sleep
from CardDeck import Card


def deal_hand(player, dealer, deck):
    """Deals the initial hands to the player and the dealer
    two cards each
    param: player: an instance of Player class
    param: dealer: an instance of  Dealer Class
    param: deck: an instance of Deck class"""
    for i in range(2):
        player.add(deck.deal())
        dealer.add(deck.deal())


def display_hands(player, dealer):
    """ Display both hands side by side with score underneath """
    print(f'\nYour hand: {player.get_hand():<30} Dealer hand: {dealer.get_hand()}')
    print(f'Your score: {str(player.score()):<29} Dealer score: {dealer.score()}')


def display_winner(player, dealer):
    if player.bust:
        print(f'\n{player.name}, you have gone BUST you lose')

    elif dealer.bust:
        print(f'\n{dealer.name}, has gone BUST you WIN. You double your stake')
        player.credits += 2

    if (not player.bust) and (not dealer.bust):
        if dealer.best_score() >= player.best_score():
            print(f'\nThe {dealer.name} WINS with a score of {dealer.best_score()}')
            dealer.credits += 2
        else:
            print(f'\n{player.name} WINS with a score of {player.best_score()}. You double your stake')
            player.credits += 2
    sleep(3)

    if dealer.credits <= 0:
        print("Congratulations! The dealer ran out of credits! You won! Game Over.")
        game_complete()
    new_hand()
    return


def game_complete():
    quit()


def player_turn(player, dealer, deck):
    """
    player : a member of Player Class
    dealer : a special member of Player Class
    returns bool: to flag if the player is bust
    """
    player.credits -= 1
    print(f"\nYour turn... {player.credits} credits remaining.")
    display_hands(player, dealer)

    # player.print_score()
    # Can only stick above 15
    while player.best_score() <= 21:  # still in play
        decision = input("\nS = STICK, T = TWIST ").upper()
        if decision == "T":
            player.add(deck.deal())  # 1 more card
            display_hands(player, dealer)
            if player.best_score() > 21:  # dealer auto wins
                player.bust = True
                break
        elif decision == "S":
            # Can only stick above 15
            if player.best_score() > 15:
                break
            else:
                print('Your total must be at least 16 to stick')
                continue
        else:
            continue
    return


def new_hand():  # leave a gap between hands
    print("-" * 80)
    print()


def computer_turn(player, dealer, deck):
    """When this function is called, the dealer's score is reset for another round, a credit is paid, the dealer's
    turn is taken and the process is displayed as text. The dealer's score remains"""

    dealer.credits -= 1
    dealer.turn = True
    sleep(1)

    print(f"\nDealer's turn...{dealer.credits} credits remaining")
    display_hands(player, dealer)

    while dealer.best_score() < 22:

        # Some simple dealer playing logic
        # if they use an ace as eleven stick if it is above 17
        if dealer.aces > 0 and dealer.best_score() >= 18:
            print("Dealer has chosen to STICK with", dealer.best_score())
            break
        # if they have no ace and the score is above 16 and not bust then stick
        elif dealer.aces == 0 and 15 < dealer.best_score() < 22:
            print("\nDealer has chosen to STICK with", dealer.best_score())
            break

        print("Dealer takes a card...")
        dealer.add(deck.deal())
        display_hands(player, dealer)
        sleep(2)

        if dealer.best_score() > 21:
            dealer.bust = True

    sleep(2)
