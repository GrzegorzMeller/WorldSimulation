from Animal import Animal
class Human(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=5
        self.initiative =4
        self.type = "HUMAN"
        self.color="BLUE"
        self.countExtraRounds=0
        self.startExtraRounds=False
        self.activateSkill=False
        self.countSkillTime=0
    def activateSkillF(self,a):
        if self.activateSkill==False:
            self.activateSkill=True
    def akcja(self, key):
        if self.startExtraRounds==True:
            self.countExtraRounds+=1
        if key == "up":
            self.posY=self.posY-1
        elif key=="down":
            self.posY=self.posY+1
        elif key=="left":
            self.posX=self.posX-1
        elif key=="right":
            self.posX=self.posX+1
        if self.activateSkill==True and self.countSkillTime<=5:
            self.countSkillTime+=1
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
    
        if self.countSkillTime>=5:
            self.activateSkill=False
            self.countSkillTime=0
            self.startExtraRounds=True
            self.world.activateToggleButton()
            
    def isAnimal(self, organism):
        if organism!="EMPTY":
            return True
        return False
