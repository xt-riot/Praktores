class Agent():
    def getBid(self):
        raise NotImplementedError("Please implent the function.")

class AllIn(Agent):
    def __init__(self, money):
        self.money = money

    def getBid(self):
        return self.money