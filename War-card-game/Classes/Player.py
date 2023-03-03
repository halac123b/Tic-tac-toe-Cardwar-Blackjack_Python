class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        # Add multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            # Add single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.add_cards)} cards.'