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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    
    #var declarations
    stack = Stack()
    visited = set()  
    path = []  

     
    if problem.isGoalState(problem.getStartState()):
        return []

    #start with first state
    stack.push((problem.getStartState(), []))

    while True:
        #check stack is empty
        if stack.isEmpty():
            return []

     
        currState, actions = stack.pop()  # take the state and the path to get the state

   
        if problem.isGoalState(currState):
            return actions  

        #check the non visited states on by one
        if currState not in visited:
            visited.add(currState)  

            
            for successorState, successorAction, successorCost in problem.getSuccessors(currState):
                newActions = actions + [successorAction]  # create a new path
                stack.push((successorState, newActions))  # keep the state and the new path

    return [] 

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()  
    visitedNodes = set()  

   
    queue.push((problem.getStartState(), []))

   
    if problem.isGoalState(problem.getStartState()): 
        return []

    while not queue.isEmpty():
       
        currentNode, path = queue.pop()

        if problem.isGoalState(currentNode):
            return path  

       
        if currentNode not in visitedNodes: #graph search technique
            visitedNodes.add(currentNode) 

            
            for successorNode, successorAction, successorCost in problem.getSuccessors(currentNode):
                newActions = path + [successorAction]  
                queue.push((successorNode, newActions)) 

    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priqueue = PriorityQueue()
    visitedNodes = set()

    priqueue.push((problem.getStartState(), [], 0), 0)

    while not priqueue.isEmpty():
        currNode, path, cost = priqueue.pop()
        
        if problem.isGoalState(currNode):
            return path
        
        if currNode not in visitedNodes:
            visitedNodes.add(currNode)
        
            for successorNode, successorAction, successorCost in problem.getSuccessors(currNode):
                newActions = path + [successorAction] 
                newCost = successorCost + cost
                newPriority = successorCost + cost #same as cost for this ucs algorith it will differ in A*

                priqueue.push((successorNode, newActions, newCost), newPriority) #add the priority so that priority queue can select from.

    return []
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
   
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    priqueue = PriorityQueue()
    visitedNodes = set()

    startNode = problem.getStartState()
    priqueue.push((startNode, [], 0), heuristic(startNode, problem))
   

    while not priqueue.isEmpty():
        currNode, path, curr_cost = priqueue.pop()
        

        if problem.isGoalState(currNode):
            return path
        
        if currNode not in visitedNodes:
            visitedNodes.add(currNode)

     
            for successorState, successorAction, successorCost in problem.getSuccessors(currNode):
                if successorState not in visitedNodes:
                    new_cost = curr_cost + successorCost  
                    new_path = path + [successorAction]
                    priority = new_cost + heuristic(successorState, problem) #priority become heuristic and the cost 
                    
                    priqueue.push((successorState, new_path, new_cost), priority) #priority queue will choose the best from cost  heuristic 

    return []






    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
