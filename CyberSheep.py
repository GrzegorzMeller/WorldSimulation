from Animal import Animal
class CyberSheep(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force = 11
        self.initiative = 4
        self.type = "CYBERSHEEP"
        self.color = "THISTLE4"
    def akcja(self):
        sosnowsky = self.world.findNearestSosnowsky(self.posY,self.posX)
        if sosnowsky['sY']==-1:
            super().akcja()
       
        elif sosnowsky['sY'] != self.posY:
            if sosnowsky['sY'] > self.posY:
                self.posY +=1
            else:
                self.posY-=1
        elif sosnowsky['sX'] != self.posX:
            if sosnowsky['sX'] > self.posX:
                self.posX+=1
            else:
                self.posX-=1
