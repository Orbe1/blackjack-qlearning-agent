
import random
from typing import Optional

from Deck import Deck
from Hand import Hand
from QLearningAgent import QLearningAgent


def train_agent(
    episodes: int = 500_000,
    learning_rate: float = 0.1,
    discount_factor: float = 1.0,
    initial_epsilon: float = 1.0,
    epsilon_decay: float = 0.9995,
    min_epsilon: float = 0.05,
    reward_bust: float = -1.0,
    reward_win: float = 1.0,
    reward_loss: float = -1.0,
    reward_tie: float = 0.0,
    q_table_filename: str = 'qtable.pkl',
    seed: Optional[int] = None,
) -> None:
    if seed is not None:
        random.seed(seed)

    agent = QLearningAgent(
        learning_rate=learning_rate,
        discount_factor=discount_factor,
        exploration_rate=initial_epsilon,
    )
    agent.load_q_table(q_table_filename)

    wins = 0
    for episode in range(episodes):
        deck = Deck()
        player = Hand()
        dealer = Hand()

        player.addCard(deck.deal())
        player.addCard(deck.deal())
        dealer.addCard(deck.deal())
        dealer.addCard(deck.deal())

        state = agent.get_state(player, dealer.cards[0])

        busted = False
        while True:
            action = agent.choose_action(state)
            if action == 'hit':
                card = deck.deal()
                if card is None:
                    deck.reset()
                    card = deck.deal()
                player.addCard(card)
                next_state = agent.get_state(player, dealer.cards[0])
                if player.getValue() > 21:
                    agent.update(state, action, reward_bust, None, terminal=True)
                    busted = True
                    break
                else:
                    agent.update(state, action, 0.0, next_state)
                    state = next_state
            else:
                break

        if not busted:
            while dealer.getValue() < 17:
                card = deck.deal()
                if card is None:
                    deck.reset()
                    card = deck.deal()
                dealer.addCard(card)

            player_val = player.getValue()
            dealer_val = dealer.getValue()

            if dealer_val > 21:
                reward = reward_win
                wins += 1
            elif player_val > dealer_val:
                reward = reward_win
                wins += 1
            elif player_val < dealer_val:
                reward = reward_loss
            else:
                reward = reward_tie

            agent.update(state, 'stand', reward, None, terminal=True)

        agent.decay_epsilon(decay_rate=epsilon_decay, min_epsilon=min_epsilon)

        if (episode + 1) % 10_000 == 0:
            win_rate = wins / (episode + 1)
            print(f"Episode {episode + 1}, Win rate: {win_rate:.4f}, Epsilon: {agent.exploration_rate:.4f}")

    agent.save_q_table(q_table_filename)
    print("Training complete.")
    print(f"Total wins: {wins} out of {episodes}")
    print(f"Q-table saved to {q_table_filename}.")


if __name__ == "__main__":
    train_agent()
