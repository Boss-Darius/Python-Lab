import Pieces
from Pieces import King


class Player:
    def __init__(self, table, color):
        self.table = table
        self.color = color
        self.currentPiece = None
        self.field = None
        self.king = None
        self.pieces = []
        self.name = None
        self.GetPieces()

    """ Sets the name for the player
        returns None
     """

    def SetName(self, name):
        self.name = name

    """ Updates the list of pieces the player has
        returns None
    """

    def GetPieces(self):
        if self.color == "white":
            self.pieces = self.table.whitePieces
        else:
            self.pieces = self.table.blackPieces

        for piece in self.pieces:
            if isinstance(piece, King.King):
                self.king = piece

    """ Checks if the player has enough pieces to checkmate the other player
        returns True if the player has enough material, False otherwise
    """

    def InsufficientMaterial(self):
        if len(self.pieces) == 1:
            return True
        elif len(self.pieces) == 2 and isinstance(self.pieces[1], Pieces.Bishop.Bishop):
            return True
        elif len(self.pieces) == 2 and isinstance(self.pieces[1], Pieces.Knight.Knight):
            return True
        else:
            return False

    """ Sets the piece the player decide to move
        returns False if the piece can't be moved, else otherwise
    """

    def SelectPiece(self, row, col):
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

    """ Sets the field where the player's piece will be moved
        returns None
    """

    def SelectField(self, row, col):
        self.field = self.table.BoardFields[8 * (7 - (row)) + col]

    """ Gets all possible moves for player
        returns a list of Field objects
    """

    def GetMoves(self):
        moves = []
        for piece in self.pieces:
            moves += piece.FilterMoves()

        return moves

    """ Checks if the player is checkmated
        returns True if the player lost the game, False otherwise
    """

    def CheckMated(self):
        return (self.king.InCheck()) and (len(self.GetMoves()) == 0)

    """ Check if the player is stalemated
        returns True if the player is stalemated, False otherwise
    """

    def StaleMated(self):
        return (not self.king.InCheck()) and (len(self.GetMoves()) == 0)
