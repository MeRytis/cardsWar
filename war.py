from random import shuffle

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
SUITS = ["Club", "Diamond", "Heart", "Spade"]


class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank}-{self.suit}"

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit: str):
        if suit not in SUITS:
            raise ValueError("Invalid suit of card")
        self._suit = suit

    @property
    def rank(self) -> str:
        return self._rank

    @rank.setter
    def rank(self, rank: str):
        if rank not in RANKS:
            raise ValueError("Invalid rank of card")
        self._rank = rank

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
    def cards(self) -> list[Card]:
        return self._cards

    @cards.setter
    def cards(self, cards: list[Card]):
        self._cards = cards

    ...


def main():
    deck = get_card_deck()

    first_player = Player(input("Player1: "), deal_cards(deck, True))
    # firstPlayer = Player("Player1", deal_cards(deck, True))

    second_player = Player(input("Player2: "), deal_cards(deck, False))
    # secondPlayer = Player("Player2", deal_cards(deck, False))

    play_game(first_player, second_player)


def get_card_deck() -> list[Card]:
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            card = Card(suit, rank)
            deck.append(card)

    shuffle(deck)
    return deck


def deal_cards(deck: list[Card], odd: bool) -> list[Card]:
    cards = []
    i = 1

    for card in deck:
        if odd and i % 2 != 0:
            cards.append(card)
        elif not odd and i % 2 == 0:
            cards.append(card)
        i += 1

    return cards


def play_game(first_player: Player, second_player: Player) -> Player:
    first_player_stash = []
    second_player_stash = []
    round = 1

    while first_player.cards and second_player.cards:
        first_player_card = first_player.cards.pop()
        second_player_card = second_player.cards.pop()

        if RANKS.index(first_player_card.rank) > RANKS.index(second_player_card.rank):
            first_player_stash.extend([first_player_card, second_player_card])
            print(
                f"Round {round}:\n{first_player.name} card {first_player_card} is higher than {second_player.name} card {second_player_card}"
            )
        elif RANKS.index(first_player_card.rank) < RANKS.index(second_player_card.rank):
            second_player_stash.extend([first_player_card, second_player_card])
            print(
                f"Round {round}:\n{second_player.name} card {second_player_card} is higher than {first_player.name} card {first_player_card}"
            )

        round += 1
        print(
            f"Result:\n{first_player.name} has {len(first_player.cards)} cards and {len(first_player_stash)} in stash\n{second_player.name} has {len(second_player.cards)} cards and {len(second_player_stash)} in stash\n"
        )


def play_war(first_player: Player, second_player: Player) -> Player: 
    ...


if __name__ == "__main__":
    main()
