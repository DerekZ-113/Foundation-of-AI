# Assignment 3

**Name**: Derek Zhang  
**NUID**: 001458122

## 1. Value Iteration
Initial state: 0
Terminal states: -2, 2
Non-terminal states: -1, 0, 1

### Iteration 1
#### State 0:
Both a1 and a2 returns a -5 reward since either result (s - 1) or (s + 1) will transit to -1 or 1 which neither is a terminal state. And this will give a reward of -5.

$$V^1_{opt}(0) = -5$$ 

#### State -1:
- a1: (0.8 x 20) + (0.2 x (-5)) = 16 - 1 = 15
- a2: (0.7 x 20) + (0.3 x (-5)) = 14 - 1.5 = 12.5
- V optimal action to state -1:
$$V^1_{opt}(-1) = max(15, 12.5) = 15$$

#### State 1:
- a1: (0.8 x (-5)) + (0.2 x 100) = -4 + 20 = 16
- a2: (0.7 x (-5)) + (0.3 x 100) = -3.5 + 30 = 26.5
- V optimal action to state 1:
$$V^1_{opt}(1) = max(16, 26.5) = 26.5$$

### Iteration 2
In this iteration, there are still the same 3 possible state to achieve, 0, -1, and 1. The calculation will be based on the previous iteration results.

#### State 0:
a1:
$$0.8 \times (-5 + V^1_{{opt}}(-1)) + 0.2 \times (-5 + V^1_{{opt}}(1)) = 0.8 \times 10 + 0.2 \times 21.5 = 12.3$$  
a2:
$$0.7 \times (-5 + V^1_{{opt}}(-1)) + 0.3 \times (-5 + V^1_{{opt}}(1)) = 0.7 \times 10 + 0.3 \times 21.5 = 13.45$$   

V optimal action to state 0:
$$V^2_{opt}(0) = max(12.3, 13.45) = 13.45$$

#### State -1:
a1:
$$0.8 \times (20) + 0.2 \times (-5 + V^1_{\text{opt}}(0)) = 16 + 0.2 \times (-10) = 14$$  
a2:
$$0.7 \times (20) + 0.3 \times (-5 + V^1_{\text{opt}}(0)) = 14 + 0.3 \times (-10) = 11$$  

V optimal action to state -1:
$$V^2_{opt}(-1) = max(14, 13) = 14$$

#### State 1:
a1:
$$0.8 \times (-5 + V^1_{opt}(0)) + 0.2 \times 100 = 0.8 \times (-10) + 20 = 12 $$

a2:
$$0.7 \times (-5 + V^1_{opt}(0)) + 0.3 \times 100 = 0.7 \times (-10) + 30 = 23$$

V optimal action to state 1:
$$V^2_{opt}(1) = max(12, 23) = 23$$

### Answer
The optimal policy for all non-terminmal states after the first iteration is:
State 0: a2 with an optimal value of 13.45
State -1: a1 with an optimal value of 14
State 1: a2 with an optimal value of 23



## 2. Transforming MDPs
### 2.1 
To convert the MDP with $\gamma < 1$ to new M' with $\gamma' = 1$, we need to find the new states, new transition probabilities, new rewards, then to the new discount factor. And we know that the actions are the same for M and M'

#### New states:
$S' = S \cup {\{\tilde s}\}$
#### Actions:
Actions a1 and a2 are the same for M and M'  

#### New transition probabilities
- For $s \in S$, transition to original states $s' \in S$:  
$P'(s, a, s') = \gamma P(s, a, s')$  

- Transition to terminal state $\tilde{s}$:  
$P' (s, a, \tilde s) = 1 - \gamma$

#### New rewards
- For $s, s' \in S$, transitions between original states:  
$R'(s, a, s') = R(s, a, s')$  

- For transition to terminal state $\tilde{s}$:  
$R'(s, a, \tilde s) = 0$

#### New discount factor:
$\gamma ' = 1$

#### Probability check
Probability in transition states: $\gamma$  
Probability transition to terminal state: $1 - \gamma$  
Total probablity balances out to 1: $\gamma + (1 - \gamma) = 1$

### 2.2 
Counterexample code is in [submission.py](../Assignment%202/Starter%20Code/submission.py)