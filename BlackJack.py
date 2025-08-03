from Deck import Deck
from Hand import Hand

class BlackJack: 
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
       
    def run(self):
        input("Welcome to Blackjack! Press Enter to start the game...")
        self.start_game()
        
    def start_game(self):
        self.deck.reset()
        self.player_hand.reset()
        self.dealer_hand.reset()
        
        for _ in range(2):
            self.player_hand.addCard(self.deck.deal())
            self.dealer_hand.addCard(self.deck.deal())
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}, Value: ?")
        print(f"Your hand: {self.player_hand.cards}, Value: {self.player_hand.getValue()}")
        self.player_turn()

    def player_turn(self):
        while True:
            choice = input("Hit or stand? (h/s): ").strip().lower()
            if choice == 'h':
                self.player_hand.addCard(self.deck.deal())
                print(f"Your hand: {self.player_hand.cards}, Value: {self.player_hand.getValue()}")
                if self.player_hand.getValue() > 21:
                    self.determine_winner()
                    return
            elif choice == 's':
                self.dealer_turn()
                self.determine_winner()
                return
            else:
                print("Invalid input. Type 'h' or 's'.")

    def dealer_turn(self):
        while self.dealer_hand.getValue() < 17:
            self.dealer_hand.addCard(self.deck.deal())
        print(f"Dealer's hand: {self.dealer_hand.cards}, Value: {self.dealer_hand.getValue()}")

    def determine_winner(self):
        player_value = self.player_hand.getValue()
        dealer_value = self.dealer_hand.getValue()
        if (dealer_value > 21 or player_value > dealer_value) and player_value <= 21:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        elif  player_value > 21:
            print("You busted! Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    while True:
        game = BlackJack()
        game.run()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            break
    print("Thanks for playing!")
