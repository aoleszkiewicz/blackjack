import random

class Deck:
    def __init__(self) -> None:
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [rank + suit for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def take_card(self) -> str:
        return self.cards.pop()

    def return_cards(self, returned_cards: list[str]) -> None:
        if not all(isinstance(card, str) for card in returned_cards):
            raise TypeError('Returned cards must be a list')

        self.cards += returned_cards
        self.shuffle()