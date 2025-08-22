class Player:
    def __init__(self) -> None:
        self.deck = []
        self.points = 0

    def add_card(self, card: str) -> None:
        """adds a card to the player's deck and assign a proper value to it."""
        self.deck.append(card)
        self.add_points(card)

    def add_points(self, card: str) -> None:
        if card[:-1] == 'A':
            while True:
                ace_point = int(input('You rolled ACE! Would you like to mark it as 1 or 11 in your deck?: '))
                if ace_point not in [1, 11]:
                    print('Invalid input. Please try again.')
                    continue
                self.points += ace_point
                break
        elif card[:-1] in ['J', 'Q', 'K']:
            self.points += 10
        else:
            self.points += int(card[:-1])

    def return_cards(self) -> list[str]:
        """return the cards from player's deck and clears itself after."""
        tmp_deck = self.deck.copy()
        self.deck = []
        return tmp_deck