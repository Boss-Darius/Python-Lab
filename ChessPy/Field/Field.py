class BoardField:
    def __init__(self, position):
        self.position = position
        self.occupied = False
        self.color = "white"

    """ Shows the representation of the field as the chess board notation
        Returns a string
    """

    def PrintPosition(self):
        return chr(65 + self.position[1]) + str(self.position[0] + 1)

    """ Changes the occupied field
        Returns None
    """

    def ChangeStatus(self):
        self.occupied = not self.occupied

    """ Sets the color for the field
        Returns None
    """

    def SetColor(self, color):
        self.color = color

    def __str__(self):
        return chr(65 + self.position[1]) + str(self.position[0] + 1)
