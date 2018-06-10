from Organism import *
import random
import math

class World(object):
    
    def __init__(self, t):
         self.tkinterWorld=t
         self.organismList=[]
         self.deadOrganisms=[]
         self.createdByMultiplication=[]

    def addOrganismToWorld(self, o):
         self.organismList.append(o)
         x = random.randint(0,self.tkinterWorld.getWidth()-1)
         y = random.randint(0,self.tkinterWorld.getHeight()-1)
         while self.tkinterWorld.checkPosition(y, x)!="WHITE":
            x = random.randint(0,self.tkinterWorld.getWidth()-1)
            y = random.randint(0,self.tkinterWorld.getHeight()-1)
         self.tkinterWorld.change_color(y,x,o.color)
         o.posY=y
         o.posX=x

    def checkOrganismOnPosition(self,aPositionY, aPositionX):
        color= self.tkinterWorld.checkPosition(aPositionY, aPositionX)
        if color=="WHITE":
            return True
        return False
    def createNewOrganism(self, newOrganismType, newOrganismPosY,newOrganismPosX):
        self.tkinterWorld.createNewOrganism(newOrganismType, newOrganismPosY,newOrganismPosX)
    def multiply(self, o):
        self.createdByMultiplication.append(o)
    
    def CheckOrganismForceOnPosition(self, y, x):
        for i in self.organismList:
            if i.getPositionY()==y and i.getPositionX()==x:
                return i.getForce()
        return 0
    def CheckOrganismTypeOnPosition(self,y,x):
        for i in self.organismList:
            if i.getPositionY()==y and i.getPositionX()==x:
                return i.getType()
        return "EMPTY"
    def getHeight(self):
        return self.tkinterWorld.getHeight()
    def getWidth(self):
        return self.tkinterWorld.getWidth()
    def addForce(self,organismType, y, x):
        for i in self.organismList:
            if i.getPositionY()==y and i.getPositionX()==x and i.getType()==organismType:
                force = i.getForce()
                force = force + 3
                i.setForce(force)
    def addOrganismToKill(self,organismType, y, x):
        for i in self.organismList:
            if i.getPositionY()==y and i.getPositionX()==x and i.getType()==organismType:
                i.setAlive(False)
                self.deadOrganisms.append(i)
                self.tkinterWorld.cleanOnPosition(i.getPositionY(),i.getPositionX())
    def activateToggleButton(self):
        self.tkinterWorld.activateToggleButton()
    def findNearestSosnowsky(self,y,x):
        distance = 100
        sY=-1
        sX=-1
        for i in self.organismList:
            if i.getType()=="SOSNOWSKY":
                a = abs(i.getPositionY()-y)
                b = abs(i.getPositionX()-x)
                c = math.sqrt((a*a) + (b*b))
                if c<distance:
                    distance =c
                    sX = i.getPositionX()
                    sY = i.getPositionY()
        return  {'sY':sY,'sX':sX}
    def newRound(self):
        for i in self.organismList:
            if i.amIAlive==True:
                age = i.getAge()
                i.setAge(age+1)
                self.tkinterWorld.cleanOnPosition(i.getPositionY(),i.getPositionX())
                save_y = i.getPositionY();
                save_x = i.getPositionX();
                if i.getType() =="HUMAN":
                    i.akcja(self.tkinterWorld.getKey())
                    self.tkinterWorld.setKey("null")
                else:
                    i.akcja()
                pom=0
                while i.getPositionY() > self.tkinterWorld.getHeight()-1 or i.getPositionY() < 0 or i.getPositionX() > self.tkinterWorld.getWidth()-1 or i.getPositionX() <0:
                    pom=pom+1
                    if pom == 100:
                        i.setPositionY(save_y)
                        i.setPositionX(save_x)
                        break
                    i.setPositionY(save_y)
                    i.setPositionX(save_x)
                    if i.getType() =="HUMAN":
                        i.akcja(self.tkinterWorld.getKey())
                        self.tkinterWorld.setKey("null")
                    else:
                        i.akcja()
                if self.tkinterWorld.checkPosition(i.getPositionY(),i.getPositionX())=="WHITE":
                    self.tkinterWorld.change_color(i.getPositionY(),i.getPositionX(), i.getColor())
                else:
                    for j in self.organismList:
                        if j.getPositionX()==i.getPositionX() and j.getPositionY()==i.getPositionY() and j.id!=i.id:
                            a = i.collision(i.getType(),i.getForce(),j.getType(),j.getForce())
                            b = j.collision(i.getType(),i.getForce(),j.getType(),j.getForce())
                            if i.getType() ==j.getType():
                                i.setPositionX(save_x)
                                i.setPositionY(save_y)
                                i.multiply(i.getPositionY(),i.getPositionX(),j.getPositionY(),j.getPositionX())
                            elif a ==True and b ==True and i.amIAlive==True and j.amIAlive==True:
                                
                                if j.getForce() > i.getForce():
                                    i.setAlive(False)
                                    self.deadOrganisms.append(i)
                                    self.tkinterWorld.cleanOnPosition(i.getPositionY(),i.getPositionX)
                                elif j.getForce() <= i.getForce():
                                    j.setAlive(False)
                                    self.deadOrganisms.append(j)
                                    #self.tkinterWorld.cleanOnPosition(j.getPositionY(), j.getPositionX)
                                    self.tkinterWorld.change_color(i.getPositionY(), i.getPositionX(), i.getColor())
                                    #to do elif when the same race/or turtle
                            elif j.getType()=="TURTLE":
                                i.setPositionX(save_x)
                                i.setPositionY(save_y)
                                self.tkinterWorld.change_color(i.getPositionY(),i.getPositionX(),i.getColor())
        for x in self.deadOrganisms:
            self.organismList.remove(x)
        del self.deadOrganisms[:]
        for x in self.createdByMultiplication:
            self.organismList.append(x)
        del self.createdByMultiplication[:]
