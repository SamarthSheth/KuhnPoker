"""
This file will contain the main game logic/rules for RPS.
"""
ROCK = 0
PAPER = 1
SCISSORS = 2

ACTIONS = ["rock", "paper", "scissors"]
NUM_ACTIONS = len(ACTIONS)

PAYOFF_MATRIX = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]       #RPS x RPS payoff matrix

def get_payoff(action1, action2) -> int:
    """
    Get payoff for Player 1.

    action1 and action2 should be integer action IDs:
    0 = rock
    1 = paper
    2 = scissors
    """
    return PAYOFF_MATRIX[action1][action2]

