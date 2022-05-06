import random


class BlackJackRules:
    SYMBOLS_NAMES = ['black_club_♣', 'red_diamond_♦', 'red_heart_♥', 'black_spade_♠']
    NAMES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    SCORE_WIN = 21
    SCORE_ACE = 11
    SCORE_ACE_MINUS = 10
    SCORE_JACK_QUEEN_KING = 10
    SCORE_DEALER_LIMIT = 17


class Deck:
    def __init__(self, symbol_name: list, name: list, quantity=1, shake=False):
        self._symbol_name = symbol_name
        self._name = name
        self._quantity = quantity
        self._deck_of_cards = self.create_deck_of_cards()
        if shake:
            self.shake()

    def __repr__(self):
        return f'{self._deck_of_cards}'

    @property
    def deck_of_cards(self) -> list[tuple]:
        return self._deck_of_cards

    @property
    def cards_in_deck(self) -> int:
        return len(self._deck_of_cards)

    def create_deck_of_cards(self) -> list[tuple]:
        deck_of_cards = []
        if self._quantity in range(1, 9):
            for i in range(len(self._symbol_name)):
                for j in range(len(self._name)):
                    for k in range(self._quantity):
                        deck_of_cards.append((self._symbol_name[i], self._name[j]))
        else:
            raise IndexError('quantity index out of range')
        return deck_of_cards

    def shake(self):
        return random.shuffle(self._deck_of_cards)

    def add_deck(self, deck: list[tuple]):
        return self._deck_of_cards.extend(deck)


class PlayerHand(BlackJackRules):
    def __init__(self):
        super().__init__()
        self._cards_in_hand = []

    def __repr__(self):
        if self._cards_in_hand:
            return f'{self._cards_in_hand}'
        else:
            return f'hand is empty'

    @property
    def in_hand(self):
        return self._cards_in_hand

    def add_card(self, card: tuple[str, str]):
        self._cards_in_hand.append(card)

    def score(self):
        score = 0
        count = 0
        for i in range(len(self._cards_in_hand)):
            try:
                score += int(self._cards_in_hand[i][1])
            except ValueError or IndexError:
                if self._cards_in_hand[i][1] == 'ace':
                    score += self.SCORE_ACE
                    if count > 1 and score > self.SCORE_WIN:
                        score -= self.SCORE_ACE_MINUS
                else:
                    score += self.SCORE_JACK_QUEEN_KING
            count += 1
        return score
