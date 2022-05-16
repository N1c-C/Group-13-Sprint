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
        player.twist(deck.deal())
        dealer.twist(deck.deal())


def display_hands(player, dealer):
    """ Displays both hands side by side with score underneath
     param: player: The current player (Player instance)
     param: dealer The current dealer (Dealer instance) """
    print(f'\nYour hand: {player.get_hand():<30} Dealer hand: {dealer.get_hand()}')
    print(f'Your score: {str(player.score()):<29} Dealer score: {dealer.score()}')


def display_winner(player, dealer):
    """Determines who has won, Checks to see if player then deal has gone bust
        If not, then compares scores and displays appropriate message.
        param: player: The current player (Player instance)
        param: dealer The current dealer (Dealer instance)"""

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
    """Quit the game"""
    quit()


def player_turn(player, dealer, deck):
    """ Loop for the players turn: Accepts keyboard input to twist or stick.
    Min stick total is 16
    param: player: current instance of Player class
    param: dealer: current instance of  Dealer Class
    param: deck: current instance of Deck class"""
    player.credits -= 1
    print(f"\nYour turn... {player.credits} credits remaining.")
    display_hands(player, dealer)

    while player.best_score() <= 21:  # still in play
        decision = input("\nS = STICK, T = TWIST ").upper()
        if decision == "T":
            player.twist(deck.deal())  # 1 more card
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


def new_hand():
    """Mark between hands with a line"""
    print("-" * 80)
    print()


def computer_turn(player, dealer, deck):
    """Function to perform dealer turn. Dealer will twist until their total is equal or greater than the player's
    Uncomment the logic to let the dealer try to avoid going bust (for a multiplayer game)
    param: player: current instance of Player class
    param: dealer: current instance of  Dealer Class
    param: deck: current instance of Deck class"""

    dealer.credits -= 1
    dealer.turn = True
    sleep(1)

    print(f"\nDealer's turn...{dealer.credits} credits remaining")
    display_hands(player, dealer)

    while dealer.best_score() < 22:

        # Some simple dealer playing logic for pontoon version un comment for multi player
        # if they use an ace as eleven stick if it is above 17
        # if dealer.aces > 0 and dealer.best_score() >= 18:
        #     print("Dealer has chosen to STICK with", dealer.best_score())
        #     break
        # if they have no ace and the score is above 16 and not bust then stick
        # elif dealer.aces == 0 and 15 < dealer.best_score() < 22:
        #     print("\nDealer has chosen to STICK with", dealer.best_score())
        #     break

        if dealer.best_score() >= player.best_score():  # comment out if using other logic
            print("Dealer has chosen to STICK with", dealer.best_score())
            break

        print("Dealer takes a card...")
        dealer.twist(deck.deal())
        display_hands(player, dealer)
        sleep(2)

        if dealer.best_score() > 21:
            dealer.bust = True

    sleep(2)
