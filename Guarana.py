from Plant import Plant
class Guarana(Plant):
    def __init__(self, w):
        super().__init__(w) 
        self.force=0
        self.initiative =0
        self.type = "GUARANA"
        self.color="BLACK"
    def collision(self, a, forceA, b, forceB):
        if a!="GUARANA":
            self.world.addForce(a, self.posY, self.posX)
        else:
            self.world.addForce(b, self.posY, self.posX)
        return True


