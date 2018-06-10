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
        
        self.world =  World(self)
        #self.wolf = Wolf(self.world)
        #self.world.addOrganismToWorld(self.wolf)
        #self.sheep = Sheep(self.world)
        #self.world.addOrganismToWorld(self.sheep)
        #self.human = Human(self.world)
        #self.world.addOrganismToWorld(self.human)
        #self.fox=Fox(self.world)
        #self.world.addOrganismToWorld(self.fox)
        #self.Turtle =Turtle(self.world)
        #self.world.addOrganismToWorld(self.Turtle)
        #self.antelope = Antelope(self.world)
        #self.world.addOrganismToWorld(self.antelope)
        #self.grass=Grass(self.world)
        #self.world.addOrganismToWorld(self.grass)
        #self.sowthistle=SowThistle(self.world)
        #self.world.addOrganismToWorld(self.sowthistle)
        #self.guarana = Guarana(self.world)
        #self.world.addOrganismToWorld(self.guarana)
        #self.blueberries=Blueberries(self.world)
        #self.world.addOrganismToWorld(self.blueberries)
        self.sosnowsky=Sosnowsky(self.world)
        self.world.addOrganismToWorld(self.sosnowsky)
        self.cyberSheep = CyberSheep(self.world)
        self.world.addOrganismToWorld(self.cyberSheep)

        self.newRoundButton=Button(self.master,text="NEW ROUND",command=lambda: self.world.newRound())
        self.newRoundButton.grid(row=100, column=100)
        self.toggleButton1=Button(self.master,text="Human Special Force", command=lambda:toggle())
        self.toggleButton1.grid(row=100, column=130)

    def change_color(self,y,x,color):
            self.buttons[y][x].config(bg=color)
    
    def initBoard(self,height,width):
        self.height = height
        self.width=width
        self.buttons=[[0 for y in range(self.height)]for x in range(self.width)]
        for y in range (0,self.height):
            for x in range (0, self.width):
                self.buttons[y][x]=Button(self.master,bg="WHITE",height=2, width=4,command=lambda y=y, x=x: self.change_color(y,x,"YELLOW"))
                self.buttons[y][x].grid(row=25+y, column=0+x)

    
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
    def createNewOrganism(self, newOrganismType, newOrganismPosY,newOrganismPosX):
        if newOrganismType=="SHEEP":
            s = Sheep(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="WOLF":
            s = Wolf(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="FOX":
            s = Fox(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="TURTLE":
            s = Turtle(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="ANTELOPE":
            s = Antelope(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="GRASS":
            s = Grass(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="SOWTHISTLE":
            s = SowThistle(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="GUARANA":
            s = Guarana(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="BLUEBERRIES":
            s = Blueberries(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="SOSNOWSKY":
            s = Sosnowsky(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)
        if newOrganismType=="CYBERSHEEP":
            s = CyberSheep(self.world)
            s.posX=newOrganismPosX
            s.posY=newOrganismPosY
            self.world.multiply(s)

root = Tk()
my_gui = TkinterWorld(root)
root.mainloop()