# **Probability, Expectation, and Decision Making Under Uncertainty**

## **Introduction**
AI systems often operate under uncertainty, requiring probabilistic reasoning to **model**, **predict**, and **make decisions** based on incomplete or noisy data. This lecture focuses on key probability concepts such as **expectation, variance, and decision-making strategies**, including **Expectiminimax**, which extends minimax to games with chance elements.

---

## **1. Probability and Random Variables**
A **random variable (X)** represents possible outcomes of a process, each with an associated probability.

### **Basic Probability Distributions**
- **Discrete Random Variable**: Takes on a finite set of values (e.g., number of heads in coin flips).
- **Continuous Random Variable**: Can take an infinite range of values (e.g., temperature readings).

### **Expectation (Expected Value)**
The **expected value** (or **mean**) of a random variable **X** represents its long-term average outcome.

\[
E[X] = \sum_{i} x_i P(X = x_i)
\]

Example:
\[
E[X] = (0 \times 0.2) + (1 \times 0.5) + (2 \times 0.3) = 1.1
\]

Expected value provides an **average prediction** but does not capture **spread (variance)**.

---

## **2. Variance and Standard Deviation**
**Variance (\(\sigma^2\))** measures how much a random variable deviates from its expected value.

\[
Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
\]

The **standard deviation** is the square root of variance:

\[
\sigma(X) = \sqrt{Var(X)}
\]

### **Example:**
For \(X = [50, 60, 55, 80, 30]\), first compute \(E[X]\), then:

1. Compute squared deviations: \((X - E[X])^2\).
2. Average them to get \(Var(X)\).
3. Take the square root to get \(\sigma(X)\).

**Intuition:**
- Higher variance = wider spread (more uncertainty).
- Lower variance = more confidence in predictions.

---

## **3. Expectiminimax: Decision Making Under Uncertainty**
The **Expectiminimax algorithm** extends **Minimax** to **games with probabilistic events**, such as **rolling dice or drawing cards**.

### **Game Tree with Chance Nodes**
Unlike **deterministic** games (e.g., chess), some games introduce **chance nodes** where outcomes are uncertain.

#### **Example Tree**
```
       MAX
      /    \
   MIN      CHANCE
  /   \       |  
  3     5   [50% 2, 50% 9]
```
- **MAX nodes** choose the **best** (highest) value.
- **MIN nodes** choose the **worst** (lowest) value.
- **Chance nodes** compute the **expected value**.

### **Algorithm Explanation**
1. **MAX Node** → Takes the **maximum** value.
2. **MIN Node** → Takes the **minimum** value.
3. **Chance Node** → Computes **expected value**:
   \[
   EV = \sum P(s) \cdot Value(s)
   \]
4. The root node decides based on **Minimax + Expectation**.

### **Python Implementation**
```python
import math

def expectiminimax(node, depth, is_max, is_chance, probabilities=None):
    if depth == 0 or isinstance(node, int):
        return node  # Terminal state or value
    
    if is_max:
        return max(expectiminimax(child, depth - 1, False, False) for child in node)
    
    elif is_chance:
        return sum(prob * expectiminimax(child, depth - 1, False, False) 
                   for child, prob in zip(node, probabilities))
    
    else:  # MIN node
        return min(expectiminimax(child, depth - 1, True, False) for child in node)

# Example tree with chance node
tree = [
    [3, 5],  # MIN layer
    [(2, 0.5), (9, 0.5)]  # CHANCE layer (probabilities: 50%-50%)
]

result = expectiminimax(tree, 2, True, False)
print("Optimal value using Expectiminimax:", result)
```

---

## **4. Probability Rules and Dependencies**
Probabilities can be dependent or independent:

### **Conditional Probability**
\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]
- **Independence**: \( P(A | B) = P(A) \) (knowing B doesn’t affect A).
- **Dependent Events**: Requires **Bayes’ Theorem**.

### **Bayes’ Theorem**
\[
P(H | E) = \frac{P(E | H) P(H)}{P(E)}
\]
Used in **AI applications** like spam detection, medical diagnosis, and speech recognition.

---

## **5. Markov Decision Processes (MDPs)**
An **MDP** models **sequential decision-making** where outcomes are probabilistic.

### **Components of an MDP**
1. **States \( S \)** - Possible situations the agent can be in.
2. **Actions \( A \)** - Actions available to the agent.
3. **Transition Model \( P(s' | s, a) \)** - Probability of moving to state \( s' \) from \( s \) after action \( a \).
4. **Reward Function \( R(s, a) \)** - Reward received for taking action \( a \).
5. **Policy \( \pi(s) \)** - Defines which action to take in each state.

### **Value Iteration for MDPs**
Value iteration finds the **optimal policy** by solving the **Bellman equation**:

\[
V(s) = \max_{a} \left[ R(s, a) + \gamma \sum_{s'} P(s' | s, a) V(s') \right]
\]

where:
- \( \gamma \) = discount factor (determines importance of future rewards).

---

## **6. Summary and Key Takeaways**
- **Expectation** is the **average value** of a random variable.
- **Variance** measures the **spread** of possible values.
- **Expectiminimax** extends **Minimax** to handle **chance nodes**.
- **Bayesian inference** updates beliefs using **probabilities**.
- **Markov Decision Processes (MDPs)** model **sequential decision-making under uncertainty**.

---

### **Next Steps: Reinforcement Learning**
- MDPs lay the foundation for **Reinforcement Learning (RL)**.
- RL agents learn **optimal policies** through experience.

---
