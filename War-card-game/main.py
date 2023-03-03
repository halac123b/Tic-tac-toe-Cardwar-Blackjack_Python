from Classes import Player
from Classes import Deck

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if (len(player_one.all_cards) == 0):
        print('Player 1 out of cards! Player 2 WINS!')
    if (len(player_two.all_cards) == 0):
        print('Player 2 out of cards! Player 1 WINS!')

    # List bài đc player rút ra và đấu với nhau
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR')
            if len(player_one.all_cards) < 3:
                print('Player 1 unable to declare a war')
                print('Player 2 wins!')
                game_on = False
            elif len(player_two.all_cards) < 3:
                print('Player 2 unable to declare a war')
                print('Player 1 wins!')
                game_on = False
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
