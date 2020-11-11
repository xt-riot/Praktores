from Agent import *
from BiddingSystem import *
from Environment import *
        

def main():
    a = AllIn(15)
    b = AllIn(32)

    firstBid = FirstBid()

    environment = Environment([a, b], biddingSystem=firstBid)
    print(environment.round())


if __name__ == "__main__":
    main()