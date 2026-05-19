"""runs everything"""

from game import ACTIONS, NUM_ACTIONS
from cfr import RPSTrainer
from utils import get_average_strategy


def main():
    trainer = RPSTrainer()
    trainer.train(100000)

    p1_avg_strategy = get_average_strategy(trainer.p1_strategy_sum)
    p2_avg_strategy = get_average_strategy(trainer.p2_strategy_sum)

    print("Player 1 average strategy:")
    for a in range(NUM_ACTIONS):
        print(f"{ACTIONS[a]}: {p1_avg_strategy[a]:.3f}")

    print("\nPlayer 2 average strategy:")
    for a in range(NUM_ACTIONS):
        print(f"{ACTIONS[a]}: {p2_avg_strategy[a]:.3f}")


if __name__ == "__main__":
    main()