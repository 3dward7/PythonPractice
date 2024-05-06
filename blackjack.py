import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ['Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def calculate_score(self, hand):
        score = 0
        num_aces = 0
        for card in hand.cards:
            if card.rank.isdigit():
                score += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                score += 10
            else:  # Ace
                num_aces += 1
                score += 11
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score

    def display_initial_hands(self):
        print("Player's Hand:", self.player_hand)
        print("Dealer's Hand:", self.dealer_hand.cards[0], "[Hidden]")

    def play(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()
        self.display_initial_hands()

        while True:
            player_score = self.calculate_score(self.player_hand)
            print("Player's Score:", player_score)

            if player_score > 21:
                print("Player busts! Dealer wins.")
                break

            action = input("Would you like to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal())
                print("Player hits.")
                print("Player's Hand:", self.player_hand)
            elif action == 's':
                print("Player stands.")
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        if player_score <= 21:
            dealer_score = self.calculate_score(self.dealer_hand)
            print("Dealer's Hand:", self.dealer_hand)
            print("Dealer's Score:", dealer_score)

            while dealer_score < 17:
                self.dealer_hand.add_card(self.deck.deal())
                print("Dealer hits.")
                print("Dealer's Hand:", self.dealer_hand)
                dealer_score = self.calculate_score(self.dealer_hand)

            if dealer_score > 21 or dealer_score < player_score:
                print("Player wins!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
