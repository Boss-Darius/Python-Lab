class BoardField:
    def __init__(self,position):
        self.position=position
        self.occupied=False
        self.color=0

    def PrintPosition(self):
        return chr(65+self.position[1])+str(self.position[0]+1)

    def ChangeStatus(self):
        self.occupied= not self.occupied

    def SetColor(self,color):
        self.color=color

    def __str__(self):
        return chr(65+self.position[1])+str(self.position[0]+1)