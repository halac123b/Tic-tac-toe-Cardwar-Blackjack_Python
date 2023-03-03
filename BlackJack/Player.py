from Classes.Deck import *
from Classes.Chip import *
from Classes.Hand import *

def take_bet(chip):
    while True:
        try:
            chip.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry please provide an integer')
        else:
            if chip.bet > chip.total:
                print('Sorry, you do not have enough chips! You have {}'.format(chip.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('Hit or stand? Enter h/s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn")
            playing = False
        else:
            print('Sorry, I did no understand that, please enter h/s only!')
            continue
        break

def show_some(player, dealer):
    # Show only ONE of dealer's card
    print("\nDealer's hand: ")
    print('First card hidden!')
    print(dealer.cards[1])
    # Show all (2) cards of player's hand
    print("\n Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # Show all cards of player and dealer
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)
    # Calculate and display value
    print(f"Value of dealer's hand is: {dealer.value}")

    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of dealer's hand is: {dealer.value}")

def player_busts(chip):
    print("BUST Player!")
    chip.lose_bet()

def player_wins(chip):
    print('Player Wins!!')
    chip.win_bet()

def dealer_busts(chip):
    print('Player wins! Dealer BUSTED!')
    chip.win_bet()

def dealer_wins(player, chip):
    print('Dealer wins!')
    chip.lose_bet()

def push():
    print('Dealer and player tie! PUSH')