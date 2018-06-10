from Plant import Plant
class Blueberries(Plant):
    def __init__(self, w):
        super().__init__(w) 
        self.force=99
        self.initiative =0
        self.type = "BLUEBERRIES"
        self.color="TURQUOISE1"
    def collision(self, a, forceA, b, forceB):
        if a!="BLUEBERRIES":
            self.world.addOrganismToKill(a, self.posY, self.posX)
        else:
            self.world.addOrganismToKill(b, self.posY, self.posX)
        return False


