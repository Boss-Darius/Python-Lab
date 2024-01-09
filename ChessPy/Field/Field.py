class BoardField:
    """
    This class implements the field of a chess board
    """

    def __init__(self, position):
        self.position = position
        self.occupied = False
        self.color = "white"

    def PrintPosition(self):
        """
        Shows the representation of the field as the chess board notation
        :return: string representing the Chess notation of the field
        """
        return chr(65 + self.position[1]) + str(self.position[0] + 1)

    def ChangeStatus(self):
        """
        Changes the occupied field
        :return: None
        """
        self.occupied = not self.occupied

    def SetColor(self, color):
        """
        Sets the color for the field
        :param color: color of the field
        :return: None
        """
        self.color = color

    def __str__(self):
        return chr(65 + self.position[1]) + str(self.position[0] + 1)
