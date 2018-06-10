from Animal import Animal
class Wolf(Animal):
    def __init__(self, w):
        super().__init__(w) 
        self.force=9
        self.initiative =5
        self.type = "WOLF"
        self.color="PINK"
    


