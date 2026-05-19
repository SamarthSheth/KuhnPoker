"""contains the CFR trainer"""

from game import NUM_ACTIONS, PAYOFF_MATRIX
from utils import regret_matching, get_average_strategy

class RPSTrainer:
    def __init__(self) -> None:
        #cumulative regrets of not playing R, P, S, respectively
        self.p1_regret_sum = [0.0 for _ in range(NUM_ACTIONS)]
        self.p2_regret_sum = [0.0 for _ in range(NUM_ACTIONS)]
        
        #cumulative strategies for each player
        self.p1_strategy_sum = [0.0 for _ in range(NUM_ACTIONS)]
        self.p2_strategy_sum = [0.0 for _ in range(NUM_ACTIONS)]
    
    def train(self, iterations):
        """
        Run regret minimization for a fixed number of iterations.
        """
        for _ in range(iterations):
            self._train_one_iteration()
    
    def _train_one_iteration(self):
        """
        Run one CFR/regret-matching update:
        1. compute current strategies from regrets,
        2. accumulate strategies,
        3. compute action utilities,
        4. update regrets.
        """
        #get curr strats for the player via regret matching:
        p1_strategy = regret_matching(self.p1_regret_sum)
        p2_strategy = regret_matching(self.p2_regret_sum)
        
        #add current strategy to cumulative strategy sum for each player:
        for a in range(NUM_ACTIONS):
            self.p1_strategy_sum[a] += p1_strategy[a]
            self.p2_strategy_sum[a] += p2_strategy[a]
        
        p1_action_utility = [0.0 for _ in range(NUM_ACTIONS)]
        p2_action_utility = [0.0 for _ in range(NUM_ACTIONS)]
        
        #compute action utilities for Player 1 given Player 2's strategy:
        for a1 in range(NUM_ACTIONS):
            utility = 0.0
            for a2 in range(NUM_ACTIONS):
                utility += PAYOFF_MATRIX[a1][a2] * p2_strategy[a2]
            p1_action_utility[a1] = utility
            
        # 4. Compute Player 1 expected utility under current strategy
        p1_expected_utility = 0.0

        for action in range(NUM_ACTIONS):
            p1_expected_utility += (
                p1_strategy[action]
                * p1_action_utility[action]
            )
        # 5. Update Player 1 regrets
        for action in range(NUM_ACTIONS):
            regret = p1_action_utility[action] - p1_expected_utility
            self.p1_regret_sum[action] += regret
        
        #compute action utilities for Player 2 given Player 1's strategy:
        for a2 in range(NUM_ACTIONS):
            utility = 0.0
            for a1 in range(NUM_ACTIONS):
                utility += (PAYOFF_MATRIX[a1][a2] * -p1_strategy[a1])
            p2_action_utility[a2] = utility
        
        #Compute Player 2 expected utility under current strategy
        p2_expected_utility = 0.0
        
        for action in range(NUM_ACTIONS):
            p2_expected_utility += (p2_strategy[action] * p2_action_utility[action])
            
        #Update Player 2 regrets
        for action in range(NUM_ACTIONS):
            regret = p2_action_utility[action] - p2_expected_utility
            self.p2_regret_sum[action] += regret

    def get_average_strategies(self, strategy_sum):
        p1_avg_strategy = get_average_strategy(self.p1_strategy_sum)
        p2_avg_strategy = get_average_strategy(self.p2_strategy_sum)

        return p1_avg_strategy, p2_avg_strategy
    
    
    
        
        