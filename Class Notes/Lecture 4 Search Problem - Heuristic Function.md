# Lecture 4: Informed Search and Heuristics  
## CS 5100 - Foundations of AI  

> Lecture 4  
> Thursday 1/16/2025  
> Chapter 3

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

Next, we will explore **heuristic design techniques and search optimizations**.
