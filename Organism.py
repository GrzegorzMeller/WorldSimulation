import uuid
class Organism(object):
    def __init__(self,w):
        self.posX=0
        self.posY=0
        self.age=0
        self.amIAlive=True
        self.id = uuid.uuid4()
        self.world=w
    def collision(self, a, forceA, b, forceB):
        return True
    def getAge(self):
        return self.age
    def setAge(self,a):
        self.age=a
    def akcja(self):
        raise NotImplementedError
    def getForce(self):
        raise NotImplementedError
    def setForce(self,a):
        raise NotImplementedError
    def getPositionY(self):
        return self.posY
    def getPositionX(self):
        return self.posX
    def setPositionY(self, a):
        self.posY=a
    def setPositionX(self,a):
        self.posX=a
    def getColor(self):
        return self.color
    def setAlive(self, a):
        self.amIAlive=a
    def getType(self):
        return self.type