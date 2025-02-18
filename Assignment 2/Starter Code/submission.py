import util, math, random
from collections import defaultdict
from util import ValueIteration

############################################################
# Problem 2.2

# If you decide 2.2 is true, prove it in your submission and put "return None" for
# the code blocks below.  If you decide that 2.2 is false, construct a counterexample.
class CounterexampleMDP(util.MDP):
    # Return a value of any type capturing the start state of the MDP.
    def startState(self):
        # BEGIN_YOUR_CODE 
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    # Return a list of strings representing actions possible from |state|.
    def actions(self, state):
        # BEGIN_YOUR_CODE 
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    # Given a |state| and |action|, return a list of (newState, prob, reward) tuples
    # corresponding to the states reachable from |state| when taking |action|.
    # Remember that if |state| is an end state, you should return an empty list [].
    def succAndProbReward(self, state, action):
        # BEGIN_YOUR_CODE 
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    # Set the discount factor (float or integer) for your counterexample MDP.
    def discount(self):
        # BEGIN_YOUR_CODE 
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

############################################################
# Problem 3

class BlackjackMDP(util.MDP):
    def __init__(self, cardValues, multiplicity, threshold, peekCost):
        """
        cardValues: list of integers (face values for each card included in the deck)
        multiplicity: single integer representing the number of cards with each face value
        threshold: maximum number of points (i.e. sum of card values in hand) before going bust
        peekCost: how much it costs to peek at the next card
        """
        self.cardValues = cardValues
        self.multiplicity = multiplicity
        self.threshold = threshold
        self.peekCost = peekCost

    # Return the start state.
    # Look closely at this function to see an example of state representation for our Blackjack game.
    # Each state is a tuple with 3 elements:
    #   -- The first element of the tuple is the sum of the cards in the player's hand.
    #   -- If the player's last action was to peek, the second element is the index
    #      (not the face value) of the next card that will be drawn; otherwise, the
    #      second element is None.
    #   -- The third element is a tuple giving counts for each of the cards remaining
    #      in the deck, or None if the deck is empty or the game is over (e.g. when
    #      the user quits or goes bust).
    def startState(self):
        return (0, None, (self.multiplicity,) * len(self.cardValues))

    # Return set of actions possible from |state|.
    # You do not need to modify this function.
    # All logic for dealing with end states should be placed into the succAndProbReward function below.
    def actions(self, state):
        return ['Take', 'Peek', 'Quit']

    # Given a |state| and |action|, return a list of (newState, prob, reward) tuples
    # corresponding to the states reachable from |state| when taking |action|.
    # A few reminders:
    # * Indicate a terminal state (after quitting, busting, or running out of cards)
    #   by setting the deck to None.
    # * If |state| is an end state, you should return an empty list [].
    # * When the probability is 0 for a transition to a particular new state,
    #   don't include that state in the list returned by succAndProbReward.
    def succAndProbReward(self, state, action):

        (stateSum, peekIndex, deckCounts) = state

        if deckCounts is None:
            return []

        if action == 'Quit':
            newState = (stateSum, None, None)
            return [(newState, 1.0, stateSum)]

        if action == 'Take':
            results = []
            if peekIndex is not None:
                cardValue = self.cardValues[peekIndex]
                newSum = stateSum + cardValue
                if newSum > self.threshold:
                    newState = (newSum, None, None)
                    results.append((newState, 1.0, 0))
                else:
                    newDeckCounts = list(deckCounts)
                    newDeckCounts[peekIndex] -= 1
                    if sum(newDeckCounts) == 0:
                        newState = (newSum, None, None)
                        reward = newSum
                    else:
                        newState = (newSum, None, tuple(newDeckCounts))
                        reward = 0
                    results.append((newState, 1.0, reward))
                return results

            totalCards = sum(deckCounts)
            for i, count in enumerate(deckCounts):
                if count <= 0:
                    continue
                cardValue = self.cardValues[i]
                prob = count / float(totalCards)
                newSum = stateSum + cardValue
                if newSum > self.threshold:
                    newState = (newSum, None, None)
                    results.append((newState, prob, 0))
                else:
                    newDeckCounts = list(deckCounts)
                    newDeckCounts[i] -= 1
                    if sum(newDeckCounts) == 0:
                        newState = (newSum, None, None)
                        reward = newSum
                    else:
                        newState = (newSum, None, tuple(newDeckCounts))
                        reward = 0
                    results.append((newState, prob, reward))
            return results

        if action == 'Peek':
            if peekIndex is not None:
                return []
            totalCards = sum(deckCounts)
            results = []
            for i, count in enumerate(deckCounts):
                if count <= 0:
                    continue
                prob = count / float(totalCards)
                newState = (stateSum, i, deckCounts)
                results.append((newState, prob, -self.peekCost))
            return results

        return []

    def discount(self):
        return 1

############################################################
# Problem 3b

def peekingMDP():
    """
    Return an instance of BlackjackMDP where peeking is the
    optimal action at least 10% of the time.
    """
    return BlackjackMDP(cardValues=[1, 5, 25], multiplicity=3, threshold=20, peekCost=1)