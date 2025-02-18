# **Probabilistic Reasoning and Decision Making in AI**

## **Introduction**
Probabilistic reasoning is essential for AI systems to handle uncertainty in real-world scenarios. Unlike deterministic approaches, probabilistic models quantify uncertainty and help AI agents make informed decisions by reasoning about the likelihood of different events.

This lecture covers **probability theory, Bayesian networks, inference algorithms**, and **decision-making under uncertainty**, following the structure of *Artificial Intelligence: A Modern Approach* Chapter 6.

---

## **Probability Theory for AI**
Probability theory provides a mathematical framework for modeling uncertainty.

### **Basic Probability Concepts**
- **Random Variables**: Variables that can take on different values based on probabilistic distributions.
- **Joint Probability Distribution**: The probability of multiple variables occurring together.
- **Conditional Probability**: The probability of an event given that another event has already occurred.
  \[
  P(A | B) = \frac{P(A \cap B)}{P(B)}
  \]
- **Bayes' Theorem**: Used to update beliefs based on new evidence.
  \[
  P(H | E) = \frac{P(E | H) P(H)}{P(E)}
  \]
  where:
  - \(P(H | E)\) is the **posterior** probability.
  - \(P(E | H)\) is the **likelihood**.
  - \(P(H)\) is the **prior** probability.
  - \(P(E)\) is the **marginal** likelihood.

---

## **Bayesian Networks**
A **Bayesian network (BN)** is a **directed acyclic graph (DAG)** that represents **causal relationships** between random variables.

### **Structure of Bayesian Networks**
- **Nodes**: Represent random variables.
- **Edges**: Represent probabilistic dependencies.
- **Conditional Probability Tables (CPTs)**: Define how each variable depends on its parent nodes.

Example BN for a **medical diagnosis system**:
```
       Flu
       |
   Fever  Cough
     \    /
      Cold
```
- The probability of having **Fever** or **Cough** depends on the probability of having **Flu** or **Cold**.
- Conditional independence simplifies calculations.

### **Example Bayesian Network: Sprinkler Model**
```
  Cloudy
   /    \
 Sprinkler  Rain
   \       /
    Wet Grass
```
- The **Wet Grass** variable depends on **Sprinkler** and **Rain**.
- If we observe **Wet Grass**, we can infer whether the **Sprinkler was on** or if it **rained**.

---

## **Probabilistic Inference in Bayesian Networks**
Inference in Bayesian networks answers queries like:
1. **Diagnostic Inference**: Given **symptoms**, determine the **disease**.
2. **Causal Inference**: Given a **cause**, predict the **effect**.
3. **Intercausal Inference**: Given multiple **causes**, adjust beliefs based on observations.

### **Exact Inference Algorithms**
1. **Enumeration Algorithm** (Computationally expensive)
2. **Variable Elimination** (Efficient for sparse networks)

### **Approximate Inference Algorithms**
For large-scale Bayesian networks, exact inference becomes infeasible. Instead, we use:
- **Monte Carlo Methods** (e.g., Gibbs Sampling)
- **Markov Chain Monte Carlo (MCMC)**
- **Particle Filtering** (Used in real-time applications like robotics)

---

## **Decision Making Under Uncertainty**
A **rational agent** makes decisions by selecting actions that maximize **expected utility**.

### **Utility Theory**
- A utility function **assigns numerical values** to different outcomes.
- **Expected Utility**:
  \[
  EU(a) = \sum_{s} P(s | a) U(s)
  \]
  where:
  - \( P(s | a) \) is the probability of reaching state \( s \) after action \( a \).
  - \( U(s) \) is the utility of state \( s \).

### **Decision Networks**
A **decision network** extends Bayesian networks by adding:
1. **Decision Nodes**: Represent agent’s actions.
2. **Utility Nodes**: Represent utility values of outcomes.

Example:
```
      Evidence
        |
  Decision → Outcome → Utility
```
A decision-making agent selects the action **that leads to the highest expected utility**.

---

## **Markov Decision Processes (MDPs)**
MDPs provide a formal framework for **sequential decision-making under uncertainty**.

### **MDP Components**
- **States \( S \)**: The set of all possible states.
- **Actions \( A \)**: The set of actions available to the agent.
- **Transition Model \( P(s' | s, a) \)**: Probability of reaching state \( s' \) given action \( a \).
- **Reward Function \( R(s, a) \)**: Immediate reward received for taking action \( a \) in state \( s \).
- **Policy \( \pi(s) \)**: The agent's strategy, mapping states to actions.

### **Bellman Equation**
The **value function** \( V(s) \) represents the expected long-term reward from state \( s \):
\[
V(s) = \max_{a} \left[ R(s, a) + \gamma \sum_{s'} P(s' | s, a) V(s') \right]
\]
where:
- \( \gamma \) is the **discount factor** (how much future rewards matter).

### **Solving MDPs**
1. **Value Iteration** (iteratively updates value function)
2. **Policy Iteration** (improves policy based on value function)

Python Implementation of **Value Iteration**:
```python
import numpy as np

def value_iteration(states, actions, transition_model, reward, gamma=0.9, theta=1e-6):
    V = {s: 0 for s in states}  # Initialize value function
    while True:
        delta = 0
        for s in states:
            max_value = float('-inf')
            for a in actions:
                sum_value = sum([transition_model[s][a][s_next] * (reward[s][a] + gamma * V[s_next])
                                for s_next in states])
                max_value = max(max_value, sum_value)
            delta = max(delta, abs(V[s] - max_value))
            V[s] = max_value
        if delta < theta:
            break
    return V

# Example usage
states = ["A", "B", "C"]
actions = ["left", "right"]
transition_model = {
    "A": {"left": {"A": 1}, "right": {"B": 1}},
    "B": {"left": {"A": 0.5, "B": 0.5}, "right": {"C": 1}},
    "C": {"left": {"B": 1}, "right": {"C": 1}}
}
reward = {"A": {"left": 0, "right": 0}, "B": {"left": 1, "right": 2}, "C": {"left": 0, "right": 3}}

optimal_values = value_iteration(states, actions, transition_model, reward)
print("Optimal Value Function:", optimal_values)
```

---

## **Conclusion**
- Bayesian networks model **uncertainty** and allow for **probabilistic inference**.
- Decision networks extend Bayesian networks to model **decision-making under uncertainty**.
- Markov Decision Processes (MDPs) provide a **framework for sequential decision-making**.
- **Value Iteration and Policy Iteration** are key methods for solving MDPs.

**Next Steps**: In future lectures, we explore **Reinforcement Learning**, which builds upon MDPs to learn optimal policies from experience.
