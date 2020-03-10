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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    stack = util.Stack() #DFS ALGO uses the LIFO.
    history = list() #list for storing the data
    empt = list() # empty list for stack
    stack.push((problem.getStartState(), empt)) #put start state in the stack and empty list 
    
    
    while util.Stack(): #DFS ALGO uses the LIFO.
        lastone=stack.pop() #Take out the very last one from the stack and store it.
        location = lastone[0]
        validirec = lastone[1]
        if location not in history: #if node is not in the list
            history.append(location) #store the node which was visited.
        if problem.isGoalState(location): #check wheter the node is in the end or not.
            return validirec #if the node is at the end, the movement to get this far from the start state will be returned.
        for a in list(problem.getSuccessors(location)):#successor(next possible state for movement), action(direction) and cost(stepcost) are in getSuccessors function
            
            if not a[0] in history: # check whether it has visited before.
                stack.push((a[0], validirec + [a[1]] )) # the movement to reach the next state and put into Queue.

    
    
    
    


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue() #BFS ALGO uses the FIFO.
    history = list() #this list for storing all the state which is visited 
    empt = list()
    queue.push((problem.getStartState(), empt)) #put start state in the stack and empty list 
    
    
    
    while util.Queue(): #loop until Queue is Empty
        lastone = queue.pop() # stor the data from the very first one from Queue
        location = lastone[0] 
        validirec = lastone[1]
        if location not in history: #if node(location) is not in the list
            history.append(location)#store the node which was visited.
        if problem.isGoalState(location): #check wheter the node is in the end or not.
            return validirec #if the node is at the end, the movement to get this far from the start state will be returned.
        for a in list(problem.getSuccessors(location)): #successor(next possible state for movement), action(direction) and cost(stepcost) are in getSuccessors function
            #print a[0]
            if not a[0] in history: #check if the state has visited before
                queue.push((a[0], validirec + [a[1]])) # the movement to reach the next state and put into Queue.
                history.append(a[0])
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priorityQ = util.PriorityQueue() #UniformCost Algo uses the prioirty Queue.
    history = list()#this list for storing all the state which is visited 
    empt = list()
    priorityQ.push([problem.getStartState(),empt,0], 0) #Put the start state and direction of movement in the empty list and cost as an item.
    
    while util.PriorityQueue(): #loop until prioirty queue is empty
        lastone = priorityQ.pop() # stor the data from the very first one from prioirty Queue
        location = lastone[0]
        validirec = lastone[1]
        cost = lastone[2]
        
        if location not in history: #if node(location) is not in the list
            history.append(location) #store the node which was visited.
            if problem.isGoalState(location): #check wheter the node is in the end or not.
                return validirec #if the node is at the end, the movement to get this far from the start state will be returned.
            for a in problem.getSuccessors(location): #successor(next possible state for movement), action(direction) and cost(stepcost) are in getSuccessors function
                priorityQ.push([a[0],validirec + [a[1]],cost+a[2]],cost+a[2])# the movement to reach the next state and cost and then put into priority Queue.
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    priorityQ1 = util.PriorityQueue() #A star Algo uses priority queue, because it compares with heuristic cost.
    history = list() #this list for storing all the state which is visited 
    empt = list()
    priorityQ1.push([problem.getStartState(),empt,0],0) #Put the start state and direction of movement in the empty list and cost as an item.
    
    while util.PriorityQueue():#loop until prioirty queue is empty
        lastone = priorityQ1.pop() # stor the data from the very first one from prioirty Queue
        location = lastone[0]
        validirec = lastone[1]
        cost = lastone[2]
        if location not in history:#if node(location) is not in the list
            history.append(location)#store the node which was visited.
            if problem.isGoalState(location): #check wheter the node is in the end or not.
                return validirec#if the node is at the end, the movement to get this far from the start state will be returned.
            for a in problem.getSuccessors(location): #successor(next possible state for movement), action(direction) and cost(stepcost) are in getSuccessors function
                if a[0] not in history or a[0] in history:# if node is not in the list OR in the list
                    hcost = heuristic(a[0], problem)#heuristic cost
                    priorityQ1.push([a[0],validirec + [a[1]],cost+a[2]],cost+a[2]+hcost)#the movement to reach the next state and cost and then put into priority Queue.
            
    return None

    util.raiseNotDefined()

    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
