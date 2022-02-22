# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """ Search the deepest nodes in the search tree first. """

    # comments for help (Keep for check status)
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # In DFS we use stack to keep track of nodes and explore from the last node visited
    frontier = util.Stack()
    # Create the list for visited nodes
    visited = []
    # Create the list for actions
    actions = []
    # Define start state
    initialState = problem.getStartState()
    # Place the starting state in the stack
    frontier.push((initialState, actions))

    while frontier:
        # Expand the last node on frontier
        currentNode, actions = frontier.pop()

        # Mark visited nodes
        if currentNode not in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            # Define sucessor list
            successors = problem.getSuccessors(currentNode)

            # Push each successor to frontier
            for state, direction, cost in successors:
                newAction = actions + [direction]
                newNode = (state, newAction)
                frontier.push(newNode)
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # In BFS we use queue to keep track of nodes and explore from the shallowest node
    frontier = util.Queue()
    # Create the list for visited nodes
    visited = []
    # Create the list for actions
    actions = []
    # Define start state
    initialState = problem.getStartState()
    # Place the starting state in the queue
    frontier.push((initialState, actions))

    while frontier:
        # Expand the last node on frontier
        currentNode, actions = frontier.pop()

        # Mark visited nodes
        if currentNode not in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            # Define sucessor list
            successors = problem.getSuccessors(currentNode)

            # Push each successor to frontier
            for state, direction, cost in successors:
                newAction = actions + [direction]
                newNode = (state, newAction)
                frontier.push(newNode)
    return actions


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    # In UCS we use priority queue to keep track of nodes and the expand order is FIFO as BFS
    frontier = util.PriorityQueue()
    # Create the list for visited nodes and we keep track of the cost
    visited = []
    # Create the list for actions
    actions = []
    # Define start state
    initialState = problem.getStartState()
    # Place the starting state in the queue
    frontier.push((initialState, actions), problem)

    while frontier:
        # Expand shallow node on frontier
        currentNode, actions = frontier.pop()

        # Mark visited nodes
        if currentNode not in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            # Define sucessor list
            successors = problem.getSuccessors(currentNode)

            # Push each successor to frontier
            for state, direction, cost in successors:
                newAction = actions + [direction]
                newCost = problem.getCostOfActions(newAction)
                frontier.push((state, newAction), newCost)
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Use a priority queue to keep track of the cost of actions with the heuristic
    frontier = util.PriorityQueue()
    # Create the list for visited nodes and we keep track of the cost
    visited = []
    # Create the list for actions
    actions = []
    # Define start state
    initialState = problem.getStartState()
    # Place the starting point in the priority queue
    frontier.push((initialState, actions), heuristic(initialState, problem))

    while frontier:
        # Expand the lowest-combined node in frontier
        currentNode, actions = frontier.pop()

        # Mark visited nodes
        if not currentNode in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            # Define sucessor list
            successors = problem.getSuccessors(currentNode)

            for state, direction, cost in successors:
                newActions = actions + [direction]
                newCost = problem.getCostOfActions(newActions) + \
                               heuristic(state, problem)
                frontier.push((state, newActions), newCost)

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
