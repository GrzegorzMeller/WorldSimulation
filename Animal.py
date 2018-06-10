from Organism import Organism
import random
class Animal(Organism):
    def __init__(self,w):
        super().__init__(w) 

    def akcja(self):
        randNewPosition = random.randint(0,7)
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

    def getForce(self):
        return self.force
    def setForce(self,a):
        self.force=a
    def multiply(self,aPositionX,aPositionY,bPositionX,bPositionY):
         y=0
         x=0
         posChagned=False
         if aPositionY==bPositionY:
            if self.world.checkOrganismOnPosition(aPositionY, aPositionX+1)==True and aPositionX+1<20:
                y=aPositionY
                x=aPositionX+1
                posChagned=True
            elif self.world.checkOrganismOnPosition(aPositionY, aPositionX-1)==True and aPositionX-1>=0:
                y=aPositionY
                x=aPositionX-1
                posChagned=True
            elif self.world.checkOrganismOnPosition(bPositionY, bPositionX+1)==True and bPositionX+1<20:
                y=bPositionY
                x=bPositionX+1
                posChagned=True
            elif self.world.checkOrganismOnPosition(bPositionY, bPositionX-1)==True and bPositionX-1>=0:
                y=bPositionY
                x=bPositionX-1
                posChagned=True
         elif aPositionX==bPositionX:
              if self.world.checkOrganismOnPosition(aPositionY+1, aPositionX)==True and aPositionY+1<20:
                y=aPositionY+1
                x=aPositionX
                posChagned=True
              elif self.world.checkOrganismOnPosition(aPositionY-1, aPositionX)==True and aPositionY-1>=0:
                y=aPositionY-1
                x=aPositionX
                posChagned=True
              elif self.world.checkOrganismOnPosition(bPositionY+1, bPositionX)==True and bPositionY+1<20:
                y=bPositionY+1
                x=bPositionX
                posChagned=True
              elif self.world.checkOrganismOnPosition(bPositionY-1, bPositionX)==True and bPositionY-1>=0:
                y=bPositionY-1
                x=bPositionX
                posChagned=True
         if posChagned==True:
             newOrganismType = self.type
             newOrganismposX=x
             newOrganismposY=y
             self.world.createNewOrganism(newOrganismType,newOrganismposY,newOrganismposX)
