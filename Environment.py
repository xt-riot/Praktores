from BiddingSystem import *
from Agent import *

class Environment:
    def __init__(self, *args, biddingSystem = BiddingSystem):
        if (len(args)) < 1:
            raise ValueError("Agents should be more than 2.")

        if (type(args[0])) == list or (type(args[0])) == tuple:
            if (len(args)) > 1:
                raise ValueError("Invalid agent insetion.")
            self.agents = self.checkType(args[0])
        else:
            if (len(args)) < 2:
                raise ValueError("Agents should be more than 2.")
            self.agents = self.checkType(args)
        
        if not isinstance(biddingSystem, BiddingSystem):
            raise TypeError(biddingSystem, "is not of type " + BiddingSystem.__name__)
        self.biddingSystem = biddingSystem

    def checkType(self, inputAgents):
        for agent in inputAgents:
            if not isinstance(agent, Agent):
                raise TypeError(agent, "is not of type " + Agent.__name__)
        return inputAgents

    def round(self):
        bids = []
        for agent in self.agents:
            bids.append(agent.getBid())

        result = self.biddingSystem.getWinner(bids)
        return result
