# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        foodDistances = [manhattanDistance(newPos, food) for food in newFood.asList()]
        nearestFoodDistance = min(foodDistances) if foodDistances else -1

 
        max_distance_to_ghost = 1
        near_ghost = 0
        num_ghosts = len(newGhostStates)

        for ghost_state, scared_time in zip(newGhostStates, newScaredTimes):
            distance = manhattanDistance(newPos, ghost_state.getPosition())
            max_distance_to_ghost += distance
            if distance <= 1 and scared_time <=  2:
                near_ghost+=1
            if distance <= 1 and scared_time >5:
               max_distance_to_ghost += 100
                


       
        return successorGameState.getScore() +1/float(nearestFoodDistance) - num_ghosts/float(max_distance_to_ghost) - near_ghost


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
 
 
        def minimax(state, depth, agentIndex):
            if depth == 0 or state.isWin() or state.isLose():
                return self.evaluationFunction(state), None
            if agentIndex == 0:
                return max(((minimax(state.generateSuccessor(agentIndex, action), depth, 1)[0], action) for action in state.getLegalActions(agentIndex)), key=lambda x: x[0])
            else:
                value = float("inf")
                for action in state.getLegalActions(agentIndex):
                    successor_state = state.generateSuccessor(agentIndex, action)
                    if agentIndex == state.getNumAgents() - 1:
                        successor_value, _ = minimax(successor_state, depth - 1, 0)
                    else:
                        successor_value, _ = minimax(successor_state, depth, agentIndex + 1)
                    value = min(value, successor_value)
                return value, None
        _, action = minimax(gameState, self.depth, 0)

        return action
       
         
        util.raiseNotDefined()       

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def AlphaBeta(state, depth, alpha, beta, agentIndex):
            if depth == 0 or state.isWin() or state.isLose() :
                return self.evaluationFunction(state), None
            if agentIndex == 0:
                value = float("-inf")
                best_action = None
                for action in state.getLegalActions(0):
                    successor_state = state.generateSuccessor(0, action)
                    successor_value, _ = AlphaBeta(successor_state, depth, alpha, beta, 1)
                    if successor_value > value:
                        value = successor_value
                        best_action = action
                    if value > beta:
                        return value, best_action
                    alpha = max(alpha, value)
                return value, best_action
            else:
                value = float("inf")
                for action in state.getLegalActions(agentIndex):
                    successor_state = state.generateSuccessor(agentIndex, action)
                    if agentIndex == state.getNumAgents() - 1:
                        successor_value, _ = AlphaBeta(successor_state, depth - 1, alpha, beta, 0)
                    else:
                        successor_value, _ = AlphaBeta(successor_state, depth, alpha, beta, agentIndex + 1)
                    value = min(value, successor_value)
                    if value < alpha:
                        return value, None
                    beta = min(beta, value)
                return value, None

        alpha = float("-inf")
        beta = float("inf")
        _, action = AlphaBeta(gameState, self.depth, alpha, beta, 0)
  
        return action
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
