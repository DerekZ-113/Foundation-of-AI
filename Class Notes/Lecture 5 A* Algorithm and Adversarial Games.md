# CS 5100 - Foundations of AI  
## Lecture 4 & 5: Informed Search, Heuristics & Introduction to Adversarial Search  
**Week 2 Thursday - 1/16/2025 & Week 3 Tuesday - 1/21/2025**  

## **Uniform Cost Search (UCS)**  
- **Complete** ✅ (Will always find a solution if one exists)  
- **Optimal** ✅ (Finds the least-cost solution)  
- **Uses a Priority Queue:** Expands the node with the lowest path cost **g(n)**.  
- **Goal test is applied when a node is expanded** rather than when generated.  
- **Time Complexity**: `O(b^(C*/E))` (C* = cost of optimal solution, E = smallest edge cost).  
- **Space Complexity**: `O(b^(C*/E))` (high if many nodes are expanded before reaching the goal).  

**Example UCS Execution (SF → San Jose)**:  
1. Start at **San Francisco**.  
2. Expand node with **lowest cost**.  
3. Continue expanding until reaching **San Jose**.  
4. Return optimal path: **San Francisco → San Mateo → Palo Alto → San Jose** (Cost: 278).  

---  

## **Informed Search Algorithms**  
Informed search uses a **heuristic function** `h(n)` to estimate the cost from node `n` to the goal.  

### **Heuristic Function (`h(n)`)**  
- Provides an estimate of the cost from a given node to the goal.  
- **Example**: Straight-line distance (Euclidean distance) to the goal.  

### **Greedy Best-First Search**  
- Expands the node with the **lowest heuristic value** `h(n)`.  
- Faster than UCS but **not optimal**.  
- **Time Complexity**: `O(b^m)` (depends on heuristic quality).  
- **Space Complexity**: `O(b^m)`.  

### **A* Search (`A*(n) = g(n) + h(n)`)**  
- Uses both **path cost (`g(n)`) and heuristic (`h(n)`)**.  
- **Optimal if `h(n)` is admissible** (never overestimates true cost).  
- **Time Complexity**: `O(b^d)` (exponential in worst case).  
- **Space Complexity**: `O(b^d)`.  

---  

## **Conditions for a Valid Heuristic**  
### **Admissibility**  
- A heuristic `h(n)` is **admissible** if it **never overestimates** the true cost to reach the goal:  
  - `h(n) ≤ h*(n)`, where `h*(n)` is the actual cost.  

### **Consistency (Monotonicity)**  
- A heuristic `h(n)` is **consistent** if:  
  - `h(n) ≤ c(n, a, n') + h(n')` for any successor `n'`.  
- **Consistency ensures A* is optimal**.  

### **Proof of Consistency Leading to Optimality**  
**Base Case:** If `n` is the goal node, then `h(n) = 0`.  
**Induction Hypothesis:** Assume `h(n') ≤ c(n, a, n') + h(n')` for nodes `n'` d steps from the goal.  
**Inductive Step:** Show it holds for `n` d+1 steps away.  
  - `h(n) ≤ c(n, a, n') + h(n')` holds for all successors `n'`.  
  - Since `h(n')` is already a lower-bound estimate, `h(n)` remains admissible.  
  - Thus, `h(n)` ensures **A* always expands nodes optimally**.  

---  

## **Why a Consistent Heuristic Leads to an Optimal Solution**  
- Guarantees that `g(n) + h(n)` never decreases along a path.  
- Ensures **A* search never reopens nodes** with a lower cost.  
- Reduces unnecessary expansions, making A* efficient.  

---  

## **Introduction to Adversarial Search (Lecture 5)**  
### **Game Theory & Search in Competitive Environments**  
- Adversarial search applies to **multi-agent environments** where agents have **conflicting goals**.  
- Most AI applications focus on **zero-sum games**, where one player's gain is another player's loss.  
- Games like **chess, Go, and poker** are well-defined adversarial search problems.  
- **Characteristics of Adversarial Games:**  
  - **Perfect information:** All game states are fully visible.  
  - **Deterministic:** No random events affecting the outcome.  
  - **Turn-taking:** Players alternate moves.  

### **Minimax Algorithm**  
- A **decision-making algorithm** used in adversarial search.  
- Assumes **both players play optimally**.  
- Evaluates possible game states and chooses the **best possible move** for the MAX player.  

**Minimax Process:**  
1. Expand the **game tree** to possible end states.  
2. Assign **utility values** to terminal states (e.g., win = +1, loss = -1, draw = 0).  
3. Apply **backward induction**:  
   - MIN selects the **lowest** utility value at its turn.  
   - MAX selects the **highest** utility value at its turn.  
4. The **root node's value determines the best move** for MAX.  

### **Alpha-Beta Pruning**  
- Optimization technique that **reduces the number of nodes evaluated**.  
- Uses **α (alpha) and β (beta) bounds** to **prune branches** that won't affect the final decision.  
- **Effectiveness:** Can reduce time complexity to `O(b^(d/2))`.  

**Alpha-Beta Pruning Process:**  
1. Traverse the **game tree** using depth-first search (DFS).  
2. Maintain **α (best choice for MAX)** and **β (best choice for MIN)**.  
3. If a node's value **exceeds the current best choice**, stop evaluating its children (prune).  
4. Continue until the optimal move is found.  

### **Why Alpha-Beta Pruning Works?**  
- Avoids searching **irrelevant branches**.  
- Significantly speeds up adversarial search.  
- **Best Case:** `O(b^(d/2))`, if nodes are evaluated optimally.  
- **Worst Case:** Still `O(b^d)`, but practical performance is much better than raw minimax.  

---  

### **Next Topic: Heuristic Evaluation in Games**  
- Evaluation functions estimate the **expected outcome of non-terminal states**.  
- Used when **full search is impractical**.  
- Example: Chess engines use a weighted sum of piece values and positional advantages.  
- Will explore **Monte Carlo Tree Search (MCTS)** and **probabilistic games** next.  
