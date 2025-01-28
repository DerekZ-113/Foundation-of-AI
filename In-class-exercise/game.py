
############################################################
# Modeling

# 2 actions can take: floor division by 2 or subtract 1

class HalvingGame(object):
    def __init__(self, N):
        self.N = N

    # state = (player, number)
    def startState(self):
        # Start code
        return (+1, self.N)
        # End code
        
    def actions(self, state):
        # Start code
        if state == 0:
            return []
        return ['/', '-']
        # End code

    def succ(self, state, action):
        # Start code
        player, number = state
        if action == '/':
            return (state // 2)
        elif action == '-': 
            return state - 1
        # End code

    def isEnd(self, state):
        # Start code
        return state == 0
        # End code


    def utility(self, state):
        # Start code

        # End code

    def player(self, state):
        # Start code

        # End code

############################################################
# Modeling

def simplePolicy(game, state):
    action = '-'
    print('simplePolicy: state {} => action {}'.format(state, action))
    return action

def humanPolicy(game, state):
    while True:
        print('humanPolicy: Enter move for state {}:'.format(state), end=' ')
        action = input().strip()
        if action in game.actions(state):
            return action

def minimaxPolicy(game, state):
    def recurse(state):
        # Return (utility of that state, action that achieves that utility)
        if game.isEnd(state):
            return (game.utility(state), None)
        # List of (utility of succ, action leading to that succ)
        candidates = [
            (recurse(game.succ(state, action))[0], action)
            for action in game.actions(state)
        ]
        player = game.player(state)
        if player == +1:
            return max(candidates)
        elif player == -1:
            return min(candidates)
        assert False

    utility, action = recurse(state)
    print('minimaxPolicy: state {} => action {} with utility {}'.format(state, action, utility))
    return action

############################################################

game = HalvingGame(N=15)
#print game.succ(game.startState(), '/')

policies = {
    +1: humanPolicy,
    #-1: simplePolicy,
    -1: minimaxPolicy,
}

state = game.startState()
while not game.isEnd(state):
    # Who controls this state?
    player = game.player(state)
    policy = policies[player]
    # Ask policy to make a move
    action = policy(game, state)
    # Advance state
    state = game.succ(state, action)

print('Final utility of game is {}'.format(game.utility(state)))
