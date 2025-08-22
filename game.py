from dealer import Dealer
from deck import Deck
from player import Player

class Game:
    def __init__(self, deck: Deck, player: Player, dealer: Dealer) -> None:
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.initialize_deck()

    def initialize_deck(self) -> None:
        """initialize a deck for both (player, dealer)."""
        self.player.add_card(self.deck.take_card())
        self.dealer.add_card(self.deck.take_card())
        self.player.add_card(self.deck.take_card())
        self.dealer.add_card(self.deck.take_card())

    def start(self) -> None:
        """starts the game."""
        while True:
            print(f'Your cards: {self.player.deck}')
            dealer_cards = ['?'] + self.dealer.deck[1:]
            print(f'Dealer cards: {dealer_cards}')
            action = input('What action would you like to do? (hit/stand): ').lower()

            if action not in ['hit', 'stand']:
                print('Invalid action, try again.')
                continue

            if action == 'hit':
                self.player.add_card(self.deck.take_card())

                if self.player.points > 21:
                    print(f'You rolled {self.player.deck[-1]}, that\'s too much, GG!')
                    break
            elif action == 'stand':
                print(f'Dealer is revealing hidden card.. it was {self.dealer.deck[0]}')

                while self.dealer.points <= 16:
                    self.dealer.add_card(self.deck.take_card())
                    print(f'Dealer rolled: {self.dealer.deck[-1]}')

                # prints the winner
                print(f'{'You' if self.player.points > self.dealer.points or self.dealer.points > 21 else 'Dealer'} won, GG.')
                self.clean_up()
                break

    def clean_up(self) -> None:
        """cleans up the deck."""
        self.deck.return_cards(self.player.deck + self.dealer.deck)