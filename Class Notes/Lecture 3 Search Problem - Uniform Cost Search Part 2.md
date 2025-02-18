# Lecture 3: Advanced Search Problems  
## CS 5100 - Foundations of AI  

> Lecture 3  
> Monday 1/13/20205  
> Chapter 3

## **Assessing Search Algorithms**
When evaluating search algorithms, we consider the following criteria:
1. **Completeness**: Will the algorithm always find a solution if one exists?
2. **Optimality**: Is the solution found the best one?
3. **Time Complexity**: How long does it take to find a solution?
4. **Space Complexity**: How much memory does it require?

---

## **Breadth-First Search (BFS)**
- **Completeness**: ✅ Yes, as long as a solution exists, BFS will find it.
- **Optimality**: ❌ Not always optimal, depends on node expansion order.
- **Time Complexity**: `O(b^d)`, where `b` is the branching factor and `d` is the depth.
- **Space Complexity**: `O(b^d)`, since BFS stores all nodes in memory at the current depth level.
- **Uses FIFO Queue:** Expands nodes layer by layer.

---

## **Depth-First Search (DFS)**
- **Completeness**: 
    - ✅ If finite states exist.
    - ❌ May fail if infinite states exist.
- **Optimality**: ❌ Not necessarily optimal.
- **Time Complexity**: `O(b^m)`, where `m` is the maximum depth.
- **Space Complexity**: `O(m)`, since only a single branch is stored at a time.
- **Uses LIFO Stack:** Explores deeper branches first before backtracking.

### **Depth-Limited Search**
- Adds a depth limit `L` to avoid infinite loops.
- **If `L < d`** → Incomplete.
- **If `L >= d`** → Complete but may not be optimal.
- Choosing `L` is challenging but can be based on problem knowledge.

### **Iterative Deepening Search (IDS)**
- Runs DFS repeatedly with increasing depth limits.
- Guarantees completeness while keeping memory usage low.
- **Time Complexity**: `O(b^d)`, slightly worse than BFS but asymptotically similar.

---

## **Uniform Cost Search (UCS)**
- Expands nodes with **lowest path cost first**.
- **Goal test is applied when a node is expanded, not generated.**
- If a better path to an existing node is found, it replaces the previous path.

### **Example Execution** (SF → San Jose)
1. Start at **San Francisco**.
2. Expand node with **lowest cost**.
3. Continue expanding until reaching **San Jose**.
4. Return optimal path: **San Francisco → San Mateo → Palo Alto → San Jose** (Cost: 278).

#### **Why is UCS Optimal?**
- **Expands nodes in order of increasing cost**.
- **First time a goal is expanded, it is the optimal path**.
- Assumes **non-negative path costs**.
- **Time Complexity**: `O(b^(C*/E))`, where `C*` is the cost of the optimal solution and `E` is the smallest edge cost.
- Can become costly if `E` is very small and `C*` is large.

---

## **Informed Search Strategies**
- UCS can be slow when edge costs are small.
- **Heuristics** can guide search more efficiently.
- Next, we explore **heuristic-based search** methods like **Greedy Best-First Search and A***.
