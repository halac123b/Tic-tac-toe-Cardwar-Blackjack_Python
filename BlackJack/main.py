from Player import *

while True:
    print('WELCOME TO BLACKJACK')

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the player's chip
    player_chips = Chip()

    # Promt the player for their bet
    take_bet(player_chips)

    # Show cards
    show_some(player_hand, dealer_hand)

    while playing:  # Recal this variable from hit_or_call function
        # Promt player for hit or stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_bust() and break out loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If player hasn't busted, play Dealer's hand until Dealer riches 17
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenario
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform player of their total chips
    print('\n Player total chips are: {}'.format(player_chips.total))
    # Ask to play again
    new_game = input('Would you like to play again? y/n: ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break
