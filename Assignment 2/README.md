# Assignment 2

**Name**: Derek Zhang  
**NUID**: 001458122

## 1. Blackjack
### 1.1 Practice with an Example
#### 1.1.1 Takes a card
Currently in the deck, there are 2 copies of 1, 1 copy of 4, and 2 copies of 7. 
So, we still have the chance to draw each of the number out in next draw randomly.  
**Draw 1**
- New hand value: 4 + 1 = 5
- New deck counts: (1, 1, 2)
- Successor state: (5, None, (1, 1, 2))
- Rewards: 0 (no bust, game continues)

**Draw 4**
- New hand value: 4 + 4 = 8
- New deck counts: (2, 0, 2)
- Successor state: (8, None, (2, 0, 2))
- Rewards: 0 (no bust, game continues)

**Draw 7**
- New hand value: 4 + 7 = 11
- New deck counts: (2, 1, 1)
- Successor state: (0, None, None)
- Rewards: 0 (busted, game over)

#### 1.1.2 Peeks a card
There are still each of the card available to draw. So there will be 3 different successor states. However, here we are just peeking. Amount of cards, and value in hand stay the same. We only update the `nextCardIndexIfPeeked()` with respective card index. The rewards for this action will be minus the peeking cost.

**Peek 1**
- Card: 1
- Index: 0
- New state: (4, 0, (2, 1, 2))
- Reward: minus peeking cost

**Peek 4**
- Card: 4
- Index: 1
- New state: (4, 1, (2, 1, 2))
- Reward: minus peeking cost

**Peek 7**
- Card: 7
- Index: 2
- New state: (4, 2, (2, 1, 2))
- Reward: minus peeking cost

#### 1.1.3 Ends the game
Current State: (4, None, (2, 1, 2))  
If we decide to end the game, we set the deck to none, and the value in hand will be the reward if it's not busted. 

- Successor state: (4, none, none)
- Reward: 4


### 1.2 Backjack MDP
#### 1.2.1 SuccAndProbReward()
Code implementation is in [submission.py](./Starter%20Code/submission.py)

#### 1.2.2 peekingMDP()
Code implementation is in [submission.py](./Starter%20Code/submission.py)


## 2. Network Parameters
### 2.1 Without Conditional Independence Assumptions
If we have n random variables and X<sub>i</sub> can take on K<sub>i</sub> values, and no conditional independence assumptions, the full joint distribution assigns a probability to every outcome in the space. 
So the total number of outcomes k<sub>1</sub> x k<sub>2</sub> x k<sub>3</sub> x ... x k<sub>n</sub>.  
Above equation shows the number of outcomes as for no conditional independence assumptions. For the number of parameters, if we assign one parameter to each outcome, the last one will be determined by all others since the probability sums up to 1, that makes the last parameter is dependent on the other parameters. So **the total number of parameters needed will be total number of outcomes minus one.**  
Answer: **k<sub>1</sub> x k<sub>2</sub> x k<sub>3</sub> x ... x k<sub>n</sub> - 1**

### 2.2 
#### 2.2.1 Hint 1: p(X<sub>1</sub>)
p(X<sub>1</sub>) is a distribution over k<sub>1</sub> outcomes. Because the probabilities need to sum up to 1. This will give us **k<sub>1</sub> - 1** independent parameters.

#### 2.2.2 Hint 2: p(X<sub>2</sub> | X<sub>1</sub>)
For every fixed value ox X<sub>1</sub> that have k<sub>1</sub> possible values, X<sub>2</sub> has k<sub>2</sub> possible outcomes. This means that for a given X<sub>1</sub>, it requires k<sub>2</sub> - 1 parameters to describe the possible outcomes of X<sub>2</sub> | X<sub>1</sub>. And this has to go with each value of X<sub>1</sub>.  
So the total number of parameters needed for **p(X<sub>2</sub> | X<sub>1</sub>) is k<sub>1</sub> x (k<sub>2</sub> - 1)**

#### 2.2.3 Total number of independent parameters for p(X<sub>i</sub> | ...)
For X<sub>1</sub>, we need **k<sub>1</sub> - 1** parameters

For 1 <= i <= m, no additional conditions, and the random variable X<sub>1</sub> depends on its ancestors X<sub>1</sub>, X<sub>2</sub>, ... , X<sub>i - 1</sub>. So the number of possible outcomes is k<sub>1</sub> x k<sub>2</sub> x ... x k<sub>(i - 1)</sub>. From previous hints we know that we need k<sub>i</sub> - 1 parameters. So the total number of parameters for each i in this range is (k<sub>1</sub> x k<sub>2</sub> x ... x k<sub>(i - 1)</sub>) x (k<sub>i</sub> - 1)  
The total parameters for this entire range will be **$\sum_{i=2}^{m}$ (k<sub>1</sub> x k<sub>2</sub> x ... x k<sub>(i - 1)</sub>) x (k<sub>i</sub> - 1)**

For i > m, X<sub>i</sub> is conditionally independent of all ancestors given the most recent ones. So the number of possible outcomes is k<sub>(i-m)</sub> x k<sub>(i-m+1)</sub> x ... x k<sub>(i-1)</sub>. For each of the outcome, k<sub>i</sub> - 1 parameters are needed. In total, for each i in this range, the number of independent parameters is: (k<sub>(i-m)</sub> x k<sub>(i-m+1)</sub> x ... x k<sub>(i-1)</sub>) x (k<sub>i</sub> - 1)  
The total parameters for this entire range will be **$\sum_{i=m+1}^{n}$ (k<sub>(i-m)</sub> x k<sub>(i-m+1)</sub> x ... x k<sub>(i-1)</sub>) x (k<sub>i</sub> - 1)**

In summary, the total number of parameters needed is to sum all the parameters up in these 3 ranges:  
i=1: k<sub>1</sub> - 1  
i=2 to i=m: $\sum_{i=2}^{m}$ (k<sub>1</sub> x k<sub>2</sub> x ... x k<sub>(i - 1)</sub>) x (k<sub>i</sub> - 1)  
i=m+1 to i=n: $\sum_{i=m+1}^{n}$ (k<sub>(i-m)</sub> x k<sub>(i-m+1)</sub> x ... x k<sub>(i-1)</sub>) x (k<sub>i</sub> - 1)  

Add up: k<sub>1</sub> - 1 + $\sum_{i=2}^{m}$ (k<sub>1</sub> x k<sub>2</sub> x ... x k<sub>(i - 1)</sub>) x (k<sub>i</sub> - 1) + $\sum_{i=m+1}^{n}$ (k<sub>(i-m)</sub> x k<sub>(i-m+1)</sub> x ... x k<sub>(i-1)</sub>) x (k<sub>i</sub> - 1)

### 2.3 Joint distribution condition
If we want the entire range i=1 to i=n to require k<sub>i</sub> - 1 parameters, we could only assume that each of the variables is independent from others. This is the only assumption we could make to achieve the starting condition i=1: k<sub>1</sub> - 1 for all the i in the entire range.