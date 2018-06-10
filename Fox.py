from Animal import Animal
import random
class Fox(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=3
        self.initiative =7
        self.type = "FOX"
        self.color="RED"

    def akcja(self):
        savePosX = self.posX
        savePosY = self.posY
        self.randNewPosition()
        while self.world.CheckOrganismForceOnPosition(savePosY,savePosX)>self.force: 
            savePosX=position_x;
            savePosY=position_y;
            randNewPosition();
        
        position_x=savePosX;
        position_y=savePosY;

    def randNewPosition(self):
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


