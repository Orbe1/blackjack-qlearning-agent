
import pickle
import random
from collections import defaultdict
from typing import Dict, List, Tuple

from Hand import Hand  

class QLearningAgent:
    ACTIONS = ['hit', 'stand']

    def __init__(
        self,
        learning_rate: float = 0.1,
        discount_factor: float = 1.0,
        exploration_rate: float = 1.0,
    ) -> None:
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table: Dict[Tuple[int, int, bool], List[float]] = defaultdict(lambda: [0.0, 0.0])

    def get_state(self, player_hand: Hand, dealer_card: str) -> Tuple[int, int, bool]:
        import re
        rank = re.match(r'\d+|[JQKA]', dealer_card).group()
        if rank in 'JQK':
            dealer_value = 10
        elif rank == 'A':
            dealer_value = 1
        else:
            dealer_value = int(rank)
        player_total = min(21, player_hand.getValue())
        usable_ace = player_hand.has_usable_ace()
        return (player_total, dealer_value, usable_ace)

    def choose_action(self, state: Tuple[int, int, bool]) -> str:
        q_values = self.q_table[state]
        if random.random() < self.exploration_rate:
            return random.choice(self.ACTIONS)
        if q_values[0] == q_values[1]:
            return random.choice(self.ACTIONS)
        return 'hit' if q_values[0] > q_values[1] else 'stand'

    def update(
        self,
        state: Tuple[int, int, bool],
        action: str,
        reward: float,
        next_state: Tuple[int, int, bool] | None,
        *,
        terminal: bool = False,
    ) -> None:
        action_idx = 0 if action == 'hit' else 1
        current_q = self.q_table[state][action_idx]
        if terminal:
            best_next = 0.0
        else:
            best_next = max(self.q_table[next_state]) if next_state is not None else 0.0
        self.q_table[state][action_idx] = current_q + self.learning_rate * (
            reward + self.discount_factor * best_next - current_q
        )

    def decay_epsilon(self, decay_rate: float = 0.9995, min_epsilon: float = 0.05) -> None:
        self.exploration_rate = max(self.exploration_rate * decay_rate, min_epsilon)

    def save_q_table(self, filename: str = 'qtable.pkl') -> None:
        with open(filename, 'wb') as f:
            pickle.dump(dict(self.q_table), f)

    def load_q_table(self, filename: str = 'qtable.pkl') -> None:
        try:
            with open(filename, 'rb') as f:
                loaded = pickle.load(f)
            self.q_table = defaultdict(lambda: [0.0, 0.0], loaded)
        except FileNotFoundError:
            self.q_table = defaultdict(lambda: [0.0, 0.0])
