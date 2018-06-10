from Plant import Plant
import random
class SowThistle(Plant):
    def __init__(self, w):
        super().__init__(w) 
        self.force=0
        self.initiative =0
        self.type = "SOWTHISTLE"
        self.color="YELLOW3"
    def akcja(self):
        for w in range(0,3):
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

