from time import sleep

from pycardgame import Deck, PlayerHand, BlackJackRules

black_jack_symbols = BlackJackRules.SYMBOLS_NAMES
black_jack_names = BlackJackRules.NAMES
black_jack_win = BlackJackRules.SCORE_WIN
black_jack_dealer_score_limit = BlackJackRules.SCORE_DEALER_LIMIT


def main():
    black_jack = Deck(black_jack_symbols, black_jack_names, shake=True, quantity=2)
    while True:
        dealer_hand = PlayerHand()
        player_hand = PlayerHand()
        turn = ''
        print('Card game Black Jack!')
        input('Click Enter for start...')
        dealer_hand.add_card(black_jack.deck_of_cards[0])
        player_hand.add_card(black_jack.deck_of_cards[1])
        dealer_hand.add_card(black_jack.deck_of_cards[2])
        player_hand.add_card(black_jack.deck_of_cards[3])
        del black_jack.deck_of_cards[:4]
        print(f'Your hand: {player_hand}')
        print(f'Your score: {player_hand.score()}')
        while turn.lower() != 'stand':
            turn = input('Your turn (Stand/Hit)... ')
            if turn.lower() == 'hit':
                if player_hand.score() < black_jack_win:
                    player_hand.add_card(black_jack.deck_of_cards[0])
                    del black_jack.deck_of_cards[0]
                    print(f'Your hand: {player_hand}')
                    print(f'Your score: {player_hand.score()}')
                if player_hand.score() > black_jack_win:
                    print('You lost =(')
                    break
                if player_hand.score() == black_jack_win:
                    print(f'Your hand: {player_hand}')
                    print(f'Your score: {player_hand.score()}')
                    print('Congratulations you win!!!')
                    break

            if turn.lower() == 'stand':
                print(f'Dealer thinking', end='')
                for i in range(3):
                    print('.', end='')
                    sleep(0.5)
                while dealer_hand.score() < black_jack_dealer_score_limit:
                    dealer_hand.add_card(black_jack.deck_of_cards[0])
                    del black_jack.deck_of_cards[0]
                print(f'\nDealer hand: {dealer_hand}')
                print(f'Dealer score: {dealer_hand.score()}')
                if dealer_hand.score() > black_jack_win:
                    print('Dealer lost. Congratulations you win!!!')
                elif player_hand.score() >= dealer_hand.score():
                    print('Congratulations you win!!!')
                else:
                    print('You lost =(')
        break


if __name__ == '__main__':
    main()
