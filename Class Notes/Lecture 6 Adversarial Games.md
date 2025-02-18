# Adversarial Search in AI

## Introduction
Adversarial search is a fundamental concept in artificial intelligence, primarily applied to competitive environments where multiple agents (often two players) have conflicting goals. This concept is widely used in game-playing AI, where decision-making is based on predicting the opponent's responses and optimizing one's own moves accordingly. This lecture note refines, expands, and organizes the content based on Lecture 6, using Chapter 5 of *Artificial Intelligence: A Modern Approach* as reference.

## Game Theory
Game theory provides the mathematical foundation for adversarial search, allowing us to model competitive decision-making scenarios. In a standard two-player, zero-sum game, one player’s gain is the other player’s loss. Some important concepts include:

- **Players:** Entities that make decisions (e.g., MAX and MIN in a minimax framework).
- **Actions:** Possible moves available to a player.
- **State Space:** The set of all possible states in the game.
- **Utility Function:** A function that assigns numerical values to terminal states, indicating the desirability of outcomes.
- **Perfect vs. Imperfect Information:** Games like chess have perfect information (both players see all moves), while games like poker involve hidden elements.

## Minimax Algorithm
The **Minimax algorithm** is the core method used in two-player, zero-sum games. It assumes both players act optimally and selects the move that maximizes the minimum possible gain.

### Algorithm Explanation
1. **Generate the game tree** to a certain depth.
2. **Evaluate terminal states** using a utility function.
3. **Propagate values upward:**
   - If it's **MAX’s turn**, select the maximum value from child nodes.
   - If it's **MIN’s turn**, select the minimum value from child nodes.
4. **The best move for MAX** at the root is the one leading to the highest minimax value.

### Example: Tic-Tac-Toe
```
       MAX
      /   \
   MIN    MIN
   / \    /  \
  3   5  2    9
```
- MAX chooses the maximum of MIN’s choices.
- MIN, playing optimally, selects the minimum from its options.
- The optimal move for MAX leads to a value of `5`.

### Python Implementation
```python
import math

def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]
    
    if isMax:
        return max(minimax(depth + 1, nodeIndex * 2, False, scores, h),
                   minimax(depth + 1, nodeIndex * 2 + 1, False, scores, h))
    else:
        return min(minimax(depth + 1, nodeIndex * 2, True, scores, h),
                   minimax(depth + 1, nodeIndex * 2 + 1, True, scores, h))

scores = [3, 5, 2, 9]
h = math.log2(len(scores))
optimal_value = minimax(0, 0, True, scores, int(h))
print("The optimal value is:", optimal_value)
```

## Alpha-Beta Pruning
The **Alpha-Beta pruning** algorithm improves minimax by eliminating branches that cannot influence the final decision. This significantly reduces the number of nodes evaluated.

### Algorithm Explanation
- **Alpha (α)** represents the best value that MAX can guarantee.
- **Beta (β)** represents the best value that MIN can guarantee.
- If β ≤ α, further exploration of that branch is unnecessary (pruning).

### Example:
```
       MAX (α=-inf, β=+inf)
      /         \
   MIN(-inf,inf)  MIN(-inf,inf)
   /   \        /     \
  3     5      2       X
```
If MAX already has a better option, it does not explore further.

### Python Implementation
```python
def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    if depth == h:
        return scores[nodeIndex]
    
    if isMax:
        value = -math.inf
        for i in range(2):
            value = max(value, alphabeta(depth + 1, nodeIndex * 2 + i, False, scores, alpha, beta, h))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = math.inf
        for i in range(2):
            value = min(value, alphabeta(depth + 1, nodeIndex * 2 + i, True, scores, alpha, beta, h))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

scores = [3, 5, 2, 9]
h = int(math.log2(len(scores)))
optimal_value = alphabeta(0, 0, True, scores, -math.inf, math.inf, h)
print("The optimal value is:", optimal_value)
```

## Heuristic Search in Adversarial Games
For complex games like Chess or Go, evaluating the full game tree is impractical. Instead, heuristic functions estimate the value of a state:

- **Material advantage** (e.g., Chess: queen=9, rook=5, knight/bishop=3, pawn=1).
- **Positional evaluation** (e.g., center control in Chess, king safety).
- **Game-specific heuristics** (e.g., potential captures in Checkers).

## Monte Carlo Tree Search (MCTS)
MCTS is another powerful approach that:
1. Simulates many random playouts from a given state.
2. Estimates state values based on win/loss statistics.
3. Uses **Upper Confidence Bound (UCB)** to balance exploration vs. exploitation.
4. Iterates over many rollouts to refine the evaluation.

MCTS has been crucial in AI breakthroughs like *AlphaGo*.

### Python Sketch of MCTS
```python
import random

def random_playout(state):
    return random.choice([1, -1])  # Simulated win/loss

def mcts(state, simulations=1000):
    results = {state: 0}
    for _ in range(simulations):
        results[state] += random_playout(state)
    return max(results, key=results.get)
```

## Conclusion
Adversarial search provides fundamental strategies for AI decision-making in games. Techniques like minimax, alpha-beta pruning, and MCTS balance computational efficiency and optimal play. Future advancements in AI-driven games leverage reinforcement learning to further improve strategic gameplay.

