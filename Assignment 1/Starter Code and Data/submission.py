from typing import List, Tuple

from mapUtil import (
    CityMap,
    computeDistance,
    createSanJoseMap,
    locationFromTag,
    makeTag, getTotalCost,
)
from util import Heuristic, SearchProblem, State, UniformCostSearch

"""
Name: Derek Zhang
NUID: 001458122
"""

"""
Question 1.1 Grid City

1. Minimum cost to reach the location.
In order to have the minimal cost to reach from (0,0) to (m,n), we need to find the shortest path, which is moving as direct as possible from the origin to the destination. 
In this grid city, we can move in four directions: east, north, west, and south. 
The cost of moving horizontally depends on current x coordinate. given by the cost function: Cost((x,y), a) = 1 + max(x,0)
The total cost of moving horizontally from 0 (origin) to m (destination) is 0, 1, 2, 3, ..., m-1. => m + m(m-1)/2
Moving vertically, the cost is always 1.

Cost moving horizontally: m(m-1)/2
Cost moving vertically: n
Total cost: m + m(m-1)/2 + n

No. the path achieving the minimal cost is not unique. Any path that moves exactly m steps horizontally and n steps vertically will always achieve the minimal cost.

2.1
False. 
Even though the grid city is infinite, UCS will terminate once it achieves the goal state at (m,n). It will explore all the relvant nodes within the grid city to find the minimum cost path.

2.2
True.
UCS will only explore the locations within the bounds (m,n) and will not explore infinite locations outside and irrelevant to the goal state.

2.3
True. UCS will always find the minimum cost path from (0,0) to (m,n) in the grid city. It will stop exploring when all nodes with a lower cost have been explored.
"""

# *IMPORTANT* :: A key part of this assignment is figuring out how to model states
# effectively. We've defined a class `State` to help you think through this, with a
# field called `memory`.
#
# As you implement the different types of search problems below, think about what
# `memory` should contain to enable efficient search!
#   > Please read the docstring for `State` in `util.py` for more details and code.

# Please also read the docstrings for the relevant classes and functions defined in `mapUtil.py`

########################################################################################
# Problem 1a: Modeling the Shortest Path Problem.





class ShortestPathProblem(SearchProblem):
    """
    Defines a search problem that corresponds to finding the shortest path
    from `startLocation` to any location with the specified `endTag`.
    """

    def __init__(self, startLocation: str, endTag: str, cityMap: CityMap):
        self.startLocation = startLocation
        self.endTag = endTag
        self.cityMap = cityMap

    def startState(self) -> State:
        # BEGIN_YOUR_CODE 
        # Set the start location using state class
        return State(location=self.startLocation)
        # END_YOUR_CODE

    def isEnd(self, state: State) -> bool:
        # BEGIN_YOUR_CODE 
        # Check if the current location has the eng tag
        tags = self.cityMap.tags[state.location]
        return any(self.endTag in tag for tag in tags)
        # END_YOUR_CODE

    def successorsAndCosts(self, state: State) -> List[Tuple[str, State, float]]:
        """
        Note we want to return a list of *3-tuples* of the form:
            (successorLocation: str, successorState: State, cost: float)
        """
        # BEGIN_YOUR_CODE 
        # Get the list of successors and their costs
        successors = []
        for nextLoc, cost in self.cityMap.distances[state.location].items():
            action = nextLoc
            nextState = State(location=nextLoc)
            successors.append((nextLoc, nextState, cost))
        return successors
        # END_YOUR_CODE


########################################################################################
# Problem 1b: Custom -- Plan a Route through San Jose


def getSanJoseShortestPathProblem() -> ShortestPathProblem:
    """
    Create your own search problem using the map of San Jose, specifying your own
    `startLocation`/`endTag`. If you prefer, you may create a new map using via
    `createCustomMap()`.

    Run `python mapUtil.py > readableSanJoseMap.txt` to dump a file with a list of
    locations and associated tags; you might find it useful to search for the following
    tag keys (amongst others):
        - `landmark=` - Hand-defined landmarks (from `data/sanjose-landmarks.json`)
        - `amenity=`  - Various amenity types (e.g., "parking_entrance", "food")
        - `parking=`  - Assorted parking options (e.g., "underground")
    """
    cityMap = createSanJoseMap()

    # Or, if you would rather use a custom map, you can uncomment the following!
    # cityMap = createCustomMap("data/custom.pbf", "data/custom-landmarks".json")

    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)

    # Set 1
    # startLocation = locationFromTag(makeTag("landmark", "city_hall"), cityMap)
    # endTag = "amenity=food"

    # Set 2
    startLocation = locationFromTag(makeTag("landmark", "northeastern_building"), cityMap)
    endTag = "parking=underground"

    
    return ShortestPathProblem(startLocation, endTag, cityMap)
    # END_YOUR_CODE

"""
1.2.2
The start location and end tag led to different paths because it reaches to the different end locations with the same tag.
The start location and end tag that couldn't yield a result was due to certain options not being available in the map.
"""


########################################################################################
# Problem 2a: Modeling the Waypoints Shortest Path Problem.


class WaypointsShortestPathProblem(SearchProblem):
    """
    Defines a search problem that corresponds to finding the shortest path from
    `startLocation` to any location with the specified `endTag` such that the path also
    traverses locations that cover the set of tags in `waypointTags`.

    Hint: naively, your `memory` representation could be a list of all locations visited.
    However, that would be too large of a state space to search over! Think 
    carefully about what `memory` should represent.
    """
    def __init__(
        self, startLocation: str, waypointTags: List[str], endTag: str, cityMap: CityMap
    ):
        self.startLocation = startLocation
        self.endTag = endTag
        self.cityMap = cityMap

        # We want waypointTags to be consistent/canonical (sorted) and hashable (tuple)
        self.waypointTags = tuple(sorted(waypointTags))

    def startState(self) -> State:
        # BEGIN_YOUR_CODE 
        visited = set()
        # The tags that are needed to be visited
        neededTags = set(self.waypointTags)
        # Add the tags of the start location to visited set if they are in the needed tags
        # So that we have count of the tags that have been visited
        for tag in self.cityMap.tags[self.startLocation]:
            if tag in neededTags:
                visited.add(tag)

        return State(location=self.startLocation, memory=frozenset(visited))
        # END_YOUR_CODE

    def isEnd(self, state: State) -> bool:
        # BEGIN_YOUR_CODE
        # Check if the current location has the end tag
        if not any(self.endTag in tag for tag in self.cityMap.tags[state.location]):
            return False

        # Check if all the required tags have been visited
        visitedSoFar = set(state.memory)
        requiredTags = set(self.waypointTags)
        # Return True if all the required tags have been visited
        return requiredTags.issubset(visitedSoFar)
        # END_YOUR_CODE

    def successorsAndCosts(self, state: State) -> List[Tuple[str, State, float]]:
        # BEGIN_YOUR_CODE 
        successors = []
        # Get the current location and already visited tags
        (currentLoc, visitedFrozenset) = (state.location, set(state.memory))
        # Get the tags that are still needed to be visited
        neededTags = set(self.waypointTags)
        
        # iterate over the successors
        for nextLoc, cost in self.cityMap.distances[currentLoc].items():
            # Create a set for visited tags
            newVisited = set(visitedFrozenset)
            # Add the matching tags from the next location to the visited set
            for tag in self.cityMap.tags[nextLoc]:
                if tag in neededTags:
                    newVisited.add(tag)
            nextState = State(location=nextLoc, memory=frozenset(newVisited))
            successors.append((nextLoc, nextState, cost))

        return successors
        # END_YOUR_CODE

"""
1.3.2 If there are n locations and k waypoint tags, what is the maximum possible number of states given a
suitable state definition for part 1 of subsection 2.3 that UCS could visit?

There are n possible locations, and k waypoint tags that can generate up to 2^k possible states.
So, the maximum possible number of states that UCS could visit is n * 2^k.
"""

########################################################################################
# Problem 2b: Custom -- Plan a Route with Unordered Waypoints through San Jose


def getSanJoseWaypointsShortestPathProblem() -> WaypointsShortestPathProblem:
    """
    Create your own search problem using the map of San Jose, specifying your own
    `startLocation`/`waypointTags`/`endTag`.

    Similar to Problem 1b, use `readableSanJoseMap.txt` to identify potential
    locations and tags.
    """
    cityMap = createSanJoseMap()
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    startLocation = locationFromTag(makeTag("landmark", "san_jose_state"), cityMap)

    # Define the waypoint tags
    waypointTags = [
        makeTag("landmark", "grocery_outlet"),
        makeTag("landmark", "seven_eleven"),
        makeTag("landmark", "northeastern_building"),
    ]

    # Define the end tag
    endTag = makeTag("landmark", "dac_phunk")

    # END_YOUR_CODE
    return WaypointsShortestPathProblem(startLocation, waypointTags, endTag, cityMap)

########################################################################################
# Problem 4a: A* to UCS reduction

# Turn an existing SearchProblem (`problem`) you are trying to solve with a
# Heuristic (`heuristic`) into a new SearchProblem (`newSearchProblem`), such
# that running uniform cost search on `newSearchProblem` is equivalent to
# running A* on `problem` subject to `heuristic`.
#
# This process of translating a model of a problem + extra constraints into a
# new instance of the same problem is called a reduction; it's a powerful tool
# for writing down "new" models in a language we're already familiar with.
# See util.py for the class definitions and methods of Heuristic and SearchProblem.


def aStarReduction(problem: SearchProblem, heuristic: Heuristic) -> SearchProblem:
    class NewSearchProblem(SearchProblem):
        def startState(self) -> State:
            # BEGIN_YOUR_CODE 
            return problem.startState()        
            # END_YOUR_CODE

        def isEnd(self, state: State) -> bool:
            # BEGIN_YOUR_CODE 
            return problem.isEnd(state)        
            # END_YOUR_CODE

        def successorsAndCosts(self, state: State) -> List[Tuple[str, State, float]]:
            # BEGIN_YOUR_CODE 
            # Get the original successors
            originalSuccessors = problem.successorsAndCosts(state)
            newSuccessors = []

            for action, nextState, cost in originalSuccessors:
                #Adjust the cost to include the heuristic
                newCost = cost + heuristic.evaluate(nextState)
                newSuccessors.append((action, nextState, newCost))
            # END_YOUR_CODE

            return newSuccessors

    return NewSearchProblem()


########################################################################################
# Problem 4b: "straight-line" heuristic for A*


class StraightLineHeuristic(Heuristic):
    """
    Estimate the cost between locations as the straight-line distance.
        > Hint: you might consider using `computeDistance` defined in `mapUtil.py`
    """
    def __init__(self, endTag: str, cityMap: CityMap):
        self.endTag = endTag
        self.cityMap = cityMap
        self.endLocations = []


        # Precompute all the Geolocations associated with endTag
        # BEGIN_YOUR_CODE
        for location, tags in cityMap.tags.items():
            if any(self.endTag in tag for tag in tags):
                self.endLocations.append(location)
        # END_YOUR_CODE

    def evaluate(self, state: State) -> float:
        # BEGIN_YOUR_CODE 
        minDistance = float('inf')
        currentLocation = state.location

        # Compute the minimum distance to any location with the endTag
        for endLocation in self.endLocations:
            if endLocation in self.cityMap.geoLocations:
                distance = computeDistance(self.cityMap.geoLocations[currentLocation], self.cityMap.geoLocations[endLocation])
                if distance < minDistance:
                    minDistance = distance

        return minDistance
        # END_YOUR_CODE