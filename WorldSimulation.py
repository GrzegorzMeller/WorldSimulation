from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from World import *
from Organism import *
from Animal import *
from Wolf import *
from Sheep import *
from Human import *
from Fox import *
from Turtle import *
from Antelope import *
from Plant import *
from Grass import *
from SowThistle import *
from Guarana import *
from Blueberries import *
from Sosnowsky import *
from CyberSheep import *

class TkinterWorld:

    def __init__(self, master):
        self.selectedAnimal=""
        self.master = master
        master.title("World")
        self.key="null"
        def leftKey(event):
           self.key="left"
        def rightKey(event):
            self.key="right"
        def upKey(event):
            self.key="up"
        def downKey(event):
            self.key="down"
        master.bind('<Left>',leftKey)
        master.bind('<Right>', rightKey)
        master.bind('<Up>', upKey)
        master.bind('<Down>',downKey)
        self.initBoard(8,8)

        def toggle():
            self.toggleButton1.config(text = "Next Human force Activation Soon")
            self.human.activateSkillF(True)
       
        def saveToFile():
            self.world.saveListToFile()
        def changeSelectedAnimal(animal):
            self.selectedAnimal=animal
        
        self.world =  World(self)
        self.wolf = Wolf(self.world)
        self.world.addOrganismToWorld(self.wolf)
        self.sheep = Sheep(self.world)
        self.world.addOrganismToWorld(self.sheep)
        self.human = Human(self.world)
        self.world.addOrganismToWorld(self.human)
        self.fox=Fox(self.world)
        self.world.addOrganismToWorld(self.fox)
        self.Turtle =Turtle(self.world)
        self.world.addOrganismToWorld(self.Turtle)
        self.antelope = Antelope(self.world)
        self.world.addOrganismToWorld(self.antelope)
        self.grass=Grass(self.world)
        self.world.addOrganismToWorld(self.grass)
        self.sowthistle=SowThistle(self.world)
        self.world.addOrganismToWorld(self.sowthistle)
        self.guarana = Guarana(self.world)
        self.world.addOrganismToWorld(self.guarana)
        self.blueberries=Blueberries(self.world)
        self.world.addOrganismToWorld(self.blueberries)
        self.sosnowsky=Sosnowsky(self.world)
        self.world.addOrganismToWorld(self.sosnowsky)
        self.cyberSheep = CyberSheep(self.world)
        self.world.addOrganismToWorld(self.cyberSheep)

        self.newRoundButton=Button(self.master,text="NEW ROUND",command=lambda: self.world.newRound())
        self.newRoundButton.grid(row=30, column=100)
        self.toggleButton1=Button(self.master,text="Human Special Force", command=lambda:toggle())
        self.toggleButton1.grid(row=30, column=110)
        self.fileButton=Button(self.master,text="Save To File", command=lambda: saveToFile())
        self.fileButton.grid(row=30,  column=120)
        self.openFileButton=Button(self.master,text="Read From File", command=lambda: self.world.readFromFile())
        self.openFileButton.grid(row=30,  column=130)

        self.wolfButton=Button(self.master,text="Wolf",command=lambda:changeSelectedAnimal("WOLF"))
        self.wolfButton.grid(row=10, column=100)
        self.sheepButton=Button(self.master,text="Sheep",command=lambda:changeSelectedAnimal("SHEEP"))
        self.sheepButton.grid(row=10, column=110)
        self.turtleButton=Button(self.master,text="Turtle",command=lambda:changeSelectedAnimal("TURTLE"))
        self.turtleButton.grid(row=10, column=120)
        self.antelopeButton=Button(self.master,text="Antelope",command=lambda:changeSelectedAnimal("ANTELOPE"))
        self.antelopeButton.grid(row=10, column=130)
        self.cyberSheepButton=Button(self.master,text="CyberSheep",command=lambda:changeSelectedAnimal("CYBERSHEEP"))
        self.cyberSheepButton.grid(row=10, column=140)

        self.grassButton=Button(self.master,text="Grass",command=lambda:changeSelectedAnimal("GRASS"))
        self.grassButton.grid(row=20, column=100)
        self.sowButton=Button(self.master,text="SowThistle",command=lambda:changeSelectedAnimal("SOWTHISTLE"))
        self.sowButton.grid(row=20, column=110)
        self.guaranaButton=Button(self.master,text="Guarana",command=lambda:changeSelectedAnimal("GUARANA"))
        self.guaranaButton.grid(row=20, column=120)
        self.blueberriesButton=Button(self.master,text="Blueberries",command=lambda:changeSelectedAnimal("BLUEBERRIES"))
        self.blueberriesButton.grid(row=20, column=130)
        self.sosnowskyButton=Button(self.master,text="Sosnowksy",command=lambda:changeSelectedAnimal("SOSNOWSKY"))
        self.sosnowskyButton.grid(row=20, column=140)

    def change_color(self,y,x,color):
            self.buttons[y][x].config(bg=color)
    
    def initBoard(self,height,width):
        self.height = height
        self.width=width
        self.buttons=[[0 for y in range(self.height)]for x in range(self.width)]
        for y in range (0,self.height):
            for x in range (0, self.width):
                self.buttons[y][x]=Button(self.master,bg="WHITE",height=2, width=4,command=lambda y=y, x=x: self.createNewOrganism(self.selectedAnimal,y,x,-1))
                self.buttons[y][x].grid(row=25+y, column=0+x)

    def cleanWholeBoard(self):
        for y in range(0,self.height):
            for x in range(0,self.width):
                self.buttons[y][x].config(bg="WHITE")
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def activateToggleButton(self):
        self.toggleButton1.config(text = "Human Special Force")
    def checkPosition(self,y,x):
        print(y," ",x)
        a= self.buttons[y][x].cget('bg')
        print(a)
        return self.buttons[y][x].cget('bg')
    def cleanOnPosition(self,y,x):
        print(y ,x)
        self.buttons[y][x].config(bg="WHITE")
    def getKey(self):
        return self.key
    def setKey(self,a):
        self.key=a
    def createNewOrganism(self, newOrganismType, newOrganismPosY,newOrganismPosX,force):
        if newOrganismType=="SHEEP":
            s = Sheep(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="WOLF":
            s = Wolf(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="FOX":
            s = Fox(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="TURTLE":
            s = Turtle(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="ANTELOPE":
            s = Antelope(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="GRASS":
            s = Grass(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="SOWTHISTLE":
            s = SowThistle(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="GUARANA":
            s = Guarana(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="BLUEBERRIES":
            s = Blueberries(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="SOSNOWSKY":
            s = Sosnowsky(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
        if newOrganismType=="CYBERSHEEP":
            s = CyberSheep(self.world)
            s.setPositionX(newOrganismPosX)
            s.setPositionY(newOrganismPosY)
            if force!=-1:
                s.setForce(force)
            self.world.multiply(s)
    def createNewHuman(self, newOrganismType, newOrganismPosY,newOrganismPosX,force,p,q):
        h = Human(self.world)
        h.setPositionX(newOrganismPosX)
        h.setPositionY(newOrganismPosY)
        h.setForce(force)
        h.setCountSkillTime(p)
        h.setCountExtraRounds(q)
        if p>0:
            h.setActivateSkill(True)
        if q>0:
            h.setStartExtraRounds(True)
        self.world.multiply(h)
root = Tk()
my_gui = TkinterWorld(root)
root.mainloop()