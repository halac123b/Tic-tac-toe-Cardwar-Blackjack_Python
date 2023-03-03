import os, sys
sys.path.append(os.path.abspath("./"))
from Card import *

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    # Lấy ra 1 lá bài
    def deal_one(self):
        return self.all_cards.pop()