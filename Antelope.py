from Animal import Animal
import random
class Antelope(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=2
        self.initiative =1
        self.type = "ANTELOPE"
        self.color="YELLOW"
    def akcja(self):
        randNewPosition = random.randint(0,7)
        if randNewPosition==0:
            self.posY=self.posY-2
            self.posX=self.posX-2
        elif randNewPosition==1:
            self.posY=self.posY-2
        elif randNewPosition==2:
            self.posY=self.posY-2
            self.posX=self.posX+2
        elif randNewPosition==3:
            self.posX=self.posX+2
        elif randNewPosition==4:
            self.posY=self.posY+2
            self.posX=self.posX+2
        elif randNewPosition==5:
            self.posY=self.posY+2
        elif randNewPosition==6:
            self.posY=self.posY+2
            self.posX=self.posX-2
        elif randNewPosition==7:
            self.posX=self.posX-2
    def collision(self, a, forceA, b, forceB):
        shouldIMove = random.randint(1,50)
        if shouldIMove>50:
            savePosX=self.posX
            savePosY=self.posY
            self.randNewPosition()
            checkPos=1;
            if savePosY<self.world.getHeight() and savePosY>=0 and savePosX<self.world.getWidth() and savePosX>0:
                checkPos = w.CheckOrganismForceOnPosition(savePosY, savePosX)
            while checkPos !=0:
                savePosX=self.posX
                savePosY=self.posY
                self.randNewPosition()
                if savePosY<self.world.getHeight() and savePosY>=0 and savePosX<self.world.getWidth() and savePosX>0:
                    checkPos = w.CheckOrganismForceOnPosition(savePosY, savePosX);
            savePosX=self.posX
            savePosY=self.posY
            return Fasle
        return True


