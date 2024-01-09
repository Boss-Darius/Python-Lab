import Pieces
from Pieces import King


class Player:
    """
    This class implements the user
    and serves as the base class for the AI class
    """

    def __init__(self, table, color):
        self.table = table
        self.color = color
        self.currentPiece = None
        self.field = None
        self.king = None
        self.pieces = []
        self.name = None
        self.GetPieces()

    def SetName(self, name):
        """
        Sets the name for the player
        :param name: the name for the player
        :return: None
        """
        self.name = name

    def GetPieces(self):
        """
        Updates the list of pieces the player has
        :return: None
        """
        if self.color == "white":
            self.pieces = self.table.whitePieces
        else:
            self.pieces = self.table.blackPieces

        for piece in self.pieces:
            if isinstance(piece, King.King):
                self.king = piece

    def InsufficientMaterial(self):
        """
        Checks if the player has enough pieces to checkmate the other player
        :return: True if the player has enough material, False otherwise
        """
        if len(self.pieces) == 1:
            return True
        elif len(self.pieces) == 2 and isinstance(self.pieces[1], Pieces.Bishop.Bishop):
            return True
        elif len(self.pieces) == 2 and isinstance(self.pieces[1], Pieces.Knight.Knight):
            return True
        else:
            return False

    def SelectPiece(self, row, col):
        """
        Sets the piece the player decides to move
        :param row: row of the piece's field
        :param col: colmun of the piece's field
        :return: False if the piece can't be moved, else otherwise
        """
        piece = self.table.GetPiece(self.table.BoardFields[8 * (7 - (row)) + col])
        if piece is None:
            print("there is no piece there")
            return False
        elif piece.color != self.color:
            print("I know it's tempting to control the enemy's pieces but chess won't allow and neither will I")
            return False
        elif piece.color == self.color and len(piece.FilterMoves()) == 0:
            print("you can move this piece")
            return False
        else:
            print("good choice")
            self.currentPiece = piece
            return True

    def SelectField(self, row, col):
        """
        Sets the field where the player's piece will be moved
        :param row: row of the field
        :param col: column for the field
        :return: None
        """
        self.field = self.table.BoardFields[8 * (7 - (row)) + col]

    def GetMoves(self):
        """
        Gets all possible moves for player
        :return: list of Field objects
        """
        moves = []
        for piece in self.pieces:
            moves += piece.FilterMoves()

        return moves

    def CheckMated(self):
        """
         Checks if the player is checkmated
        :return: True if the player lost the game, False otherwise
        """
        return (self.king.InCheck()) and (len(self.GetMoves()) == 0)

    def StaleMated(self):
        """
        Check if the player is stalemated
        :return: True if the player is stalemated, False otherwise
        """
        return (not self.king.InCheck()) and (len(self.GetMoves()) == 0)
