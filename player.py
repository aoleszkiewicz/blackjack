class Player:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: str):
        """adds a card to the player's deck."""
        if not isinstance(card, str):
            raise TypeError('Card must be a string')

        self.deck.append(card)

    def return_cards(self):
        """return the cards from player's deck and clears itself after."""
        tmp_deck = self.deck.copy()
        self.deck = []
        return tmp_deck