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

    def SelectPiece(self):
        piecesICanMove = []

        for piece in self.pieces:
            if piece.FilterMoves() != []:
                piecesICanMove += [piece]

        # seed(1)
        index = randint(0, len(piecesICanMove) - 1)

        self.currentPiece = piecesICanMove[index]

    def SelectField(self):
        # seed(1)
        moves = self.currentPiece.FilterMoves()
        index = randint(0, len(moves) - 1)
        self.field = moves[index]

    def Move(self):
        self.SelectPiece()
        self.SelectField()
        self.currentPiece.Move(self.field, self.currentPiece.FilterMoves())
