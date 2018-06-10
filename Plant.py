from Organism import Organism
import random
class Plant(Organism):
    def __init__(self,w):
        super().__init__(w) 
    def akcja(self):
        shouldImultiply = random.randint(0,100)
        if shouldImultiply>=96:
            randNewPosition = random.randint(0,7)
            newOrganismposY = self.posY
            newOrganismposX = self.posX
            if randNewPosition==0:
                newOrganismposY=self.posY-1
                newOrganismposX=self.posX-1
            elif randNewPosition==1:
                newOrganismposY=self.posY-1
            elif randNewPosition==2:
                newOrganismposY=self.posY-1
                newOrganismposX=self.posX+1
            elif randNewPosition==3:
                newOrganismposX=self.posX+1
            elif randNewPosition==4:
                newOrganismposY=self.posY+1
                newOrganismposX=self.posX+1
            elif randNewPosition==5:
                newOrganismposY=self.posY+1
            elif randNewPosition==6:
                newOrganismposY=self.posY+1
                newOrganismposX=self.posX-1
            elif randNewPosition==7:
                newOrganismposX=self.posX-1
            if newOrganismposX<self.world.getWidth() and newOrganismposX>=0 and newOrganismposY<self.world.getHeight() and newOrganismposY>=0: 
                if self.world.checkOrganismOnPosition(newOrganismposY, newOrganismposX)==True:
                    self.world.createNewOrganism(self.type,newOrganismposY,newOrganismposX)
    def getForce(self):
        return self.force
    def multiply(self,aPositionX,aPositionY,bPositionX,bPositionY):
        return 0
