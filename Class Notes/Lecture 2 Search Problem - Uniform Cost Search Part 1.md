# Lecture 2 Search Problem - Uniform Cost Search
## CS 5100 - Foundations of AI  

> Lecture 2  
> Thursday 1/9/20205  
> Chapter 3

## **Introduction to Search Problems**
Search problems involve **finding solutions** to computational problems by exploring possible states and transitions. 

### **Examples**:
- **Route finding problems**
- **Games (e.g., Chess, Go)**

## **Defining a Search Problem**
A search problem consists of the following elements:

1. **Initial State**: The starting location.
2. **Actions**: Available actions that can be taken (e.g., from San Jose, one can go west or north).
3. **Transition Model**: Defines how states transition based on actions.
4. **Cost Function**: Quantifies the cost of transitioning from one state to another.
5. **Goal Test**: Determines if a given state is the goal.

---

## **Tree Search Algorithm (Pseudocode)**
```python
def tree_search(start_node):
    frontier = {start_node}  # Nodes yet to be explored
    explored = set()  # Nodes that have been visited
    
    while len(frontier) > 0:
        node = frontier.pop()  # Choose and remove a node from the frontier
        
        if node in explored:
            continue  # Skip already explored nodes
        
        if is_goal(node):
            return "Solution Found"
        
        explored.add(node)
        frontier.update(get_successors(node))
    
    return "Failure - No Solution Found"
```

### **Notes on Tree Search**
- The **frontier** stores nodes yet to be explored.
- The **explored set** keeps track of visited nodes.
- Avoids infinite loops by ensuring nodes are not revisited.
- Uses a function `is_goal(node)` that returns **True** if the node is the goal.

---

## **Criteria to Assess Search Algorithms**
1. **Completeness**: Will the algorithm always find a solution if one exists?
2. **Optimality**: Is the solution found the best one?
3. **Time Complexity**: How long does it take to find a solution?
4. **Space Complexity**: How much memory does it require?

---

## **Breadth-First Search (BFS)**
BFS explores nodes **layer by layer** before moving deeper.

### **Complexity Analysis**:
- **Completeness**: ✅ Yes, BFS always finds a solution if one exists.
- **Optimality**: ❌ Not always optimal, depends on node expansion order.
- **Time Complexity**: `O(b^d)` where `b` is the branching factor and `d` is the depth.
- **Space Complexity**: `O(b^d)` since all nodes at the current depth are stored.

```plaintext
Graph Representation:

          (San Jose)
         /        \  
  (Palo Alto)   (Fremont)
     /     \          | 
(SF)  (Redwood)   (Oakland)
```

---

## **Depth-First Search (DFS)**
DFS explores a branch **fully** before backtracking.

### **Complexity Analysis**:
- **Completeness**: 
    - ✅ If finite states exist.
    - ❌ May fail if infinite states exist.
- **Optimality**: ❌ Not necessarily optimal.
- **Time Complexity**: `O(b^m)`, where `m` is the maximum depth.
- **Space Complexity**: `O(m)` since only a single branch is stored at a time.

```plaintext
Graph Representation (DFS traversal example):

    (San Jose)
        |
   (Palo Alto)
        |
  (Redwood City)
        |
  (San Francisco)
```

---

## **Depth-Limited Search & Iterative Deepening Search**
- **Depth-Limited Search**: Limits depth to `L`.
    - **If `L < d`** → Incomplete.
    - **If `L >= d`** → Complete.
    
- **Iterative Deepening Search (IDS)**: 
    - Repeatedly applies DFS with increasing depth limits (`L = 0, 1, 2...`)
    - **Time Complexity**: `O(b^d)` (asymptotically same as BFS)
    - Resolves DFS’s infinite path issue while maintaining low space complexity.

---

## **Uniform Cost Search (UCS)**
- Expands nodes with **lowest path cost first**.
- **Goal test** is applied when a node is selected for expansion.
- If a better path to an existing node is found, it replaces the previous path.

### **Example Execution**:
1. Start at **San Francisco**.
2. Expand node with **lowest cost**.
3. Continue expanding until reaching **San Jose**.
4. Return optimal path: **San Francisco → San Mateo → Palo Alto → San Jose** (Cost: 278).

---

## **Why UCS is Optimal?**
- UCS **expands nodes in order of increasing cost**.
- The **first time a goal is expanded**, it is guaranteed to be the optimal path.
- **Assumption**: Step costs are non-negative.

---

## **Next Steps: Informed Search Strategies**
- UCS can be **inefficient** if step costs are too small.
- We will introduce **heuristics** to improve efficiency.

---

This markdown document contains **structured notes and visual representations** of search problems and algorithms. Let me know if you need further refinements! 🚀
