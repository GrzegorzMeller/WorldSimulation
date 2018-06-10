from Plant import Plant
class Grass(Plant):
    def __init__(self, w):
        super().__init__(w) 
        self.force=0
        self.initiative =0
        self.type = "GRASS"
        self.color="GRAY83"
    



