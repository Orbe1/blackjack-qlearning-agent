# Blackjack Q-Learning Agent 🂡

This project implements a tabular Q-learning agent to learn how to play Blackjack using reinforcement learning.

The agent learns an optimal hit/stand policy through self-play, gradually improving by exploring the state space and updating a Q-table.

## Features

- Simplified Blackjack logic (no splits/doubles)
- Customizable reward structure
- Persistent Q-table saved using `pickle`
- Epsilon-greedy exploration with decay
- Clean separation of game logic and agent logic

## Files

- `Deck.py` – Card deck logic
- `Hand.py` – Player and dealer hand management
- `QLearningAgent.py` – Q-learning logic
- `trainAgent.py` – Training script
- `BlackJack.py` – (Optional) Script for playing the game manually or testing
- `qtable.pkl` – Saved Q-table for future reuse

## Usage

To train the agent:

```bash
python trainAgent.py
