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
### 2.1 

### 2.2

### 2.3