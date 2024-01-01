import Pieces.King
import  copy
from Field import Field


class Piece:
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PrintPosition(self):
        return self.field.PrintPosition()

    def AttackMoves(self):
        return self.PossibleMoves

    def CanCapture(self, row, col):
        chessboard = self.table.BoardFields
        if (self.color == "white" and chessboard[ 8 * (7 - (row)) + col] in self.table.BlackPiecesFields()):
            # print("capture for white")
            # we can't capture the kings
            if not (isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col]), Pieces.King.King)): return True
        elif (self.color == "black" and chessboard[8 * (7 - (row)) + col] in self.table.WhitePiecesFields()):
            # print("capture for black")
            # we can't capture the kings
            if not (isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col]), Pieces.King.King)): return True
        else:
            # print("not capturing")
            return False

    def ShowPossibleMoves(self):
        possibleMoves = []
        for possibleMove in self.PossibleMoves():
            possibleMoves += [str(possibleMove)]

        # print(possibleMoves)
        return possibleMoves

    def FilterMoves(self):

        movesList = self.PossibleMoves()
        filteredMoves = []
        originalRow,originalCol=self.field.position
        for move in movesList:
            itermediateState = copy.deepcopy(self.table)
            # print("stare curenta")
            # print(itermediateState)
            # print("am aratat starea curenta")
            # print()

            myKing = None
            if self.color == "white":
                for piece in itermediateState.whitePieces:
                    if isinstance(piece, Pieces.King.King):
                        myKing = piece
                        break
            else:
                for piece in itermediateState.blackPieces:
                    if isinstance(piece, Pieces.King.King):
                        myKing = piece
                        break

            row = move.position[0]
            col = move.position[1]

            pieceIMove = itermediateState.GetPiece(itermediateState.BoardFields[8 * (7 - (originalRow)) + originalCol])
            print(pieceIMove)
            pieceIMove.Move(itermediateState.BoardFields[8 * (7 - (row)) + col], pieceIMove.PossibleMoves())

            # print("stare intermediara")
            # print(itermediateState)
            # print("am aratat starea intermediara")
            if not myKing.InCheck():
                filteredMoves += [move]
                print(move," mutare valida")
            else: print(move," mutare invalida")
        return filteredMoves

    def ShowFilteredMoves(self):
        filteredMoves = []
        for filteredMove in self.FilterMoves():
            filteredMoves += [str(filteredMove)]

        # print(filteredMoves)
        return filteredMoves

    def Warning(self):
        return "That is not a correct move for this piece"
    def Move(self, newfield,moves):
        if newfield in moves:
            if newfield.occupied:
                self.table.RemovePiece(self.table.GetPiece(newfield))
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
        else:
            print(self.Warning())
