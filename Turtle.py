from Animal import Animal
import random
class Turtle(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=2
        self.initiative =1
        self.type = "TURTLE"
        self.color="GREEN"
    def akcja(self):
        shouldIMove = random.randint(1,75)
        if shouldIMove >75:
            randNewPosition=ranom.randint(0,7)
            if randNewPosition==0:
                self.posY=self.posY-1
                self.posX=self.posX-1
            elif randNewPosition==1:
                self.posY=self.posY-1
            elif randNewPosition==2:
                self.posY=self.posY-1
                self.posX=self.posX+1
            elif randNewPosition==3:
                self.posX=self.posX+1
            elif randNewPosition==4:
                self.posY=self.posY+1
                self.posX=self.posX+1
            elif randNewPosition==5:
                self.posY=self.posY+1
            elif randNewPosition==6:
                self.posY=self.posY+1
                self.posX=self.posX-1
            elif randNewPosition==7:
                self.posX=self.posX-1
    def collision(self, a, forceA, b, forceB):
        if a !="TURTLE":
            if forceA> 5:
                return False
        else:
            if forceB >5:
                return False
        return True



