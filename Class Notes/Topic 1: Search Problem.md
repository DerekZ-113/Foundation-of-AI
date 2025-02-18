# **CS 5100 - Foundations of AI**  
## **Topic 1: Search Problems**  

### **1. Introduction to Search Problems**  
In artificial intelligence, **search** is the process of exploring and finding a path from an initial state to a goal state. This is fundamental in AI applications such as **pathfinding, robotics, planning, and games**.

A **search problem** consists of:  
1. **Initial State (`s0`)**: The starting condition of the problem.  
2. **Actions (`A(s)`)**: The set of available actions from each state.  
3. **Transition Model (`T(s, a)`)**: The result of applying an action to a state.  
4. **Goal Test (`G(s)`)**: Determines whether a given state is a goal state.  
5. **Path Cost Function (`g(n)`)**: Assigns a numerical cost to each solution path.  

A solution is a **sequence of actions** leading from the **initial state to the goal state** with an optimal or acceptable cost.

---

## **2. Uninformed Search Algorithms (Blind Search)**  
Uninformed search algorithms **do not use additional problem-specific knowledge** beyond the problem definition.

### **2.1 Breadth-First Search (BFS)**
- Explores nodes **layer by layer**, expanding all nodes at depth `d` before `d+1`.
- **Complete** ✅ (Finds a solution if one exists).
- **Optimal** ✅ for unit-cost problems.
- **Time Complexity**: `O(b^d)`, where `b` is the branching factor and `d` is depth.
- **Space Complexity**: `O(b^d)`, as it stores all nodes at the current level.
- **Uses a FIFO queue (First-In, First-Out).**

#### **Implementation (Python)**
```python
from collections import deque

def bfs(initial_state, goal_test, successors):
    queue = deque([(initial_state, [])])  # Store (state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()

        if goal_test(state):
            return path  # Return the path to the goal
        
        if state not in visited:
            visited.add(state)
            for action, next_state in successors(state):
                queue.append((next_state, path + [action]))

    return None  # No solution found
```

---

### **2.2 Depth-First Search (DFS)**
- Explores a **branch fully** before backtracking.
- **Complete** ❌ (Fails in infinite state spaces).
- **Optimal** ❌ (May not find the best solution).
- **Time Complexity**: `O(b^m)`, where `m` is the max depth.
- **Space Complexity**: `O(m)`, since it only stores nodes along the current path.
- **Uses a LIFO stack (Last-In, First-Out).**

#### **Implementation (Python)**
```python
def dfs(initial_state, goal_test, successors):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if goal_test(state):
            return path  # Solution found

        if state not in visited:
            visited.add(state)
            for action, next_state in successors(state):
                stack.append((next_state, path + [action]))

    return None  # No solution found
```

---

### **2.3 Uniform-Cost Search (UCS)**
- Expands nodes with the **lowest path cost** `g(n)`.
- **Complete** ✅.
- **Optimal** ✅ (if all step costs are positive).
- **Time Complexity**: `O(b^(C*/E))`, where `C*` is the optimal cost and `E` is the smallest edge cost.
- **Space Complexity**: `O(b^(C*/E))`.
- **Uses a priority queue (min-heap).**

#### **Implementation (Python)**
```python
import heapq

def ucs(initial_state, goal_test, successors):
    pq = [(0, initial_state, [])]  # (cost, state, path)
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if goal_test(state):
            return path  # Solution found

        if state not in visited:
            visited.add(state)
            for action, next_state, action_cost in successors(state):
                heapq.heappush(pq, (cost + action_cost, next_state, path + [action]))

    return None  # No solution found
```

---

## **3. Informed Search Algorithms (Heuristic Search)**
Informed search algorithms **use heuristic functions** to estimate the best path to the goal.

### **3.1 Greedy Best-First Search**
- Expands nodes with the **lowest heuristic value** `h(n)`.
- **Not Optimal** ❌ but fast.
- **Time Complexity**: `O(b^m)`.
- **Space Complexity**: `O(b^m)`.
- **Uses a priority queue.**

#### **Implementation (Python)**
```python
def greedy_best_first_search(initial_state, goal_test, successors, heuristic):
    pq = [(heuristic(initial_state), initial_state, [])]  # (heuristic, state, path)
    visited = set()

    while pq:
        _, state, path = heapq.heappop(pq)

        if goal_test(state):
            return path  # Solution found

        if state not in visited:
            visited.add(state)
            for action, next_state in successors(state):
                heapq.heappush(pq, (heuristic(next_state), next_state, path + [action]))

    return None  # No solution found
```

---

### **3.2 A* Search (`f(n) = g(n) + h(n)`)**
- Expands nodes based on both **path cost (`g(n)`) and heuristic (`h(n)`)**.
- **Complete** ✅.
- **Optimal** ✅ if `h(n)` is **admissible**.
- **Time Complexity**: `O(b^d)`.
- **Space Complexity**: `O(b^d)`.
- **Uses a priority queue.**

#### **Implementation (Python)**
```python
def a_star_search(initial_state, goal_test, successors, heuristic):
    pq = [(heuristic(initial_state), 0, initial_state, [])]  # (f(n), g(n), state, path)
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if goal_test(state):
            return path  # Solution found

        if state not in visited or visited[state] > g:
            visited[state] = g
            for action, next_state, action_cost in successors(state):
                new_g = g + action_cost
                new_f = new_g + heuristic(next_state)
                heapq.heappush(pq, (new_f, new_g, next_state, path + [action]))

    return None  # No solution found
```

---

## **4. Evaluating Search Algorithms**
| Algorithm  | Complete? | Optimal? | Time Complexity | Space Complexity |
|------------|----------|----------|----------------|----------------|
| BFS  | ✅ | ✅ (if uniform) | `O(b^d)` | `O(b^d)` |
| DFS  | ❌ | ❌ | `O(b^m)` | `O(m)` |
| UCS  | ✅ | ✅ | `O(b^(C*/E))` | `O(b^(C*/E))` |
| A*   | ✅ | ✅ (if `h(n)` is admissible) | `O(b^d)` | `O(b^d)` |
| Greedy | ✅ | ❌ | `O(b^m)` | `O(b^m)` |

---

