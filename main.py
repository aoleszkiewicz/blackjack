from dealer import Dealer
from deck import Deck
from game import Game
from player import Player

def main() -> None:
    deck = Deck()
    player = Player()
    dealer = Dealer()

    game = Game(deck=deck, player=player, dealer=dealer)
    game.start()

if __name__ == '__main__':
    main()