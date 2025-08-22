from player import Player

class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()

    def add_points(self, card: str) -> None:
        if card[:-1] == 'A':
            self.points += (11 if self.points + 11 <= 21 else 1)
        elif card[:-1] in ['J', 'Q', 'K']:
            self.points += 10
        else:
            self.points += int(card[:-1])