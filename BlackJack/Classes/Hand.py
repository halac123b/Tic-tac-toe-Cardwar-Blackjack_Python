from Classes.Card import *

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # Nếu tổng lớn hơn 21, Ace sẽ là 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
