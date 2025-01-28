import sys
import util
sys.setrecursionlimit(10000)
### Model (search problem)
class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    def startState(self):
        # START CODE
        return 1
        # END CODE
    def isEnd(self, state):
        # START CODE
        return state == self.N
        # END CODE

    def succAndCost(self, state):
        # Returns list of (action, newState, cost) triples
        # START CODE
        result = []

        if state + 1 <= self.N:
            result.append(('plus_one', state + 1, 1))

        if state * 2 <= self.N:
            result.append(('mult_by_2', state * 2, 2))
        
        return result 
        # END CODE
