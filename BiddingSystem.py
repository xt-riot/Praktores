class BiddingSystem:
    def getWinner(self, bids):
        raise NotImplementedError("Not implemented.")

class FirstBid(BiddingSystem):
    def __init__(self):
        pass

    def getWinner(self, bids):
        f = lambda i: bids[i]
        maxIdx = max(range(len(bids)), key=f)
        
        response = []
        for i in range(len(bids)):
            isWinner = i == maxIdx
            response.append([isWinner, bids[maxIdx]])
        return response