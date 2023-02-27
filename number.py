import random

class Number_game:
    def __init__(self,round):
        if round==1:
            self.max=10
        elif round==3:
            self.max=50
        else:
            self.max=100
        self.computer=random.choice([i for i in range(1,self.max+1)])
        # print(self.computer)
    def result(self,player):
        self.player=player
        if self.player>self.computer:
            return 'Greater number'
        elif self.player<self.computer:
            return 'lesser number'
        else:
            return 'You won'
