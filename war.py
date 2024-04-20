ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Club", "Diamond", "Heart", "Spade"]


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit: str):
        if suit not in suits:
            raise ValueError("Invalid suit of card")
        self._suit = suit

    @property
    def rank(self) -> str:
        return self._rank

    @rank.setter
    def rank(self, rank: str):
        if rank not in ranks:
            raise ValueError("Invalid rank of card")
        self._rank

    ...


class Person:
    def __init__(self, name: str) -> None:
        self.name = name.capitalize()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    ...


class Player(Person):
    def __init__(self, name: str, cards: list[Card]) -> None:
        super().__init__(name)
        self.cards = cards

    @property
    def cards(self) -> list[cards]:
        return self._cards

    @cards.setter
    def cards(self, cards: list[cards]):
        self._cards = cards

    ...


def main():
    deck = get_card_deck()
    ...


def get_card_deck() -> list[Card]: ...


def play_game(firstPlayer: Player, secondPlayer: Player) -> Player: ...


def play_war(firstPlayer: Player, secondPlayer: Player) -> Player: ...


if __name__ == "__main__":
    main()
