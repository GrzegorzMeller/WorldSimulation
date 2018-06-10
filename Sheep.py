from Animal import Animal
class Sheep(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=4
        self.initiative =4
        self.type = "SHEEP"
        self.color="GRAY"



