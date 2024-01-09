from Players import Player
from random import seed
from random import randint


class AI(Player.Player):
    def __init__(self, table, color):
        self.table = table
        self.color = color
        self.currentPiece = None
        self.field = None
        self.king = None
        self.pieces = []
        self.name = self.color + "Bot"

    """ Sets the piece for the AI as a random piece the AI has that can be moved
        returns None
    """

    def SelectPiece(self):
        piecesICanMove = []

        for piece in self.pieces:
            if piece.FilterMoves() != []:
                piecesICanMove += [piece]

        # seed(1)
        index = randint(0, len(piecesICanMove) - 1)

        self.currentPiece = piecesICanMove[index]

    """ Sets a random field where the piece of the AI can move
        returns None
    """

    def SelectField(self):
        # seed(1)
        moves = self.currentPiece.FilterMoves()
        index = randint(0, len(moves) - 1)
        self.field = moves[index]

    """ Moves the AI's piece to the selected field
        returns None
    """

    def Move(self):
        self.SelectPiece()
        self.SelectField()
        self.currentPiece.Move(self.field, self.currentPiece.FilterMoves())
