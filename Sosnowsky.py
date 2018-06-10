from Plant import Plant
import random
class Sosnowsky(Plant):
    def __init__(self, w):
        super().__init__(w) 
        self.force=10
        self.initiative =0
        self.type = "SOSNOWSKY"
        self.color="PURPLE"

    def collision(self, a, forceA, b, forceB):
        if a!="SOSNOWSKY" and a!="CYBERSHEEP":
            self.world.addOrganismToKill(a, self.posY, self.posX)
        elif a!="CYBERSHEEP":
            self.world.addOrganismToKill(b, self.posY, self.posX)
        elif a=="CYBERSHEEP":
            return True
        return False
    def akcja(self):
        super().akcja()
        savePosX = self.posX
        savePosY = self.posY
        savePosY-=1
        savePosX-=1
        a = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)
        if self.isAnimal(a): 
            self.world.addOrganismToKill(a, savePosY,savePosX)
        savePosX+=1 
        b= self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)
        if self.isAnimal(b): 
            self.world.addOrganismToKill(b, savePosY,savePosX)
        savePosX+=1
        c = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)  
        if self.isAnimal(c): 
            self.world.addOrganismToKill(c, savePosY,savePosX)
        savePosY+=1
        d = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)
        if self.isAnimal(d):
            self.world.addOrganismToKill(d, savePosY,savePosX)
        savePosY+=1
        e = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)  
        if self.isAnimal(e): 
            self.world.addOrganismToKill(e, savePosY,savePosX)
        savePosX-=1
        f = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX) 
        if self.isAnimal(f):
            self.world.addOrganismToKill(f, savePosY,savePosX)
        savePosX-=1
        g = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX)
        if self.isAnimal(g):
            self.world.addOrganismToKill(g, savePosY,savePosX)
        savePosY-=1
        h = self.world.CheckOrganismTypeOnPosition(savePosY, savePosX) 
        if self.isAnimal(h):
            self.world.addOrganismToKill(h, savePosY,savePosX) 
        savePosX+=1

    def isAnimal(self,animalName):
        if animalName!="SONSOWSKY" and animalName!="BLUEBERRIES"and animalName!="GUARANA"and animalName!="GRASS"and animalName!="EMPTY" and animalName!="SOWTHISTLE" and animalName!="CYBERSHEEP":
            return True
        return False


