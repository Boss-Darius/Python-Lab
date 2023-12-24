from Field import Field


class Piece:
    def __init__(self, position, color):
        self.field = Field.BoardField(position)
        self.field.occupied = True
        self.color = color

    def PrintPosition(self):
        return self.field.PrintPosition()

    def AttackMoves(self):
        return self.PossibleMoves
    def CanCapture(self, row, col):
        chessboard = self.table.BoardFields
        if (self.color == "white" and chessboard[
            8 * (7 - (row)) + col] in self.table.BlackPiecesFields()):
            # print("capture for white")
            return True
        elif (self.color == "black" and chessboard[
            8 * (7 - (row)) + col] in self.table.WhitePiecesFields()):
            # print("capture for black")
            return True
        else:
            # print("not capturing")
            return False

    def Move(self, newfield):
        if not newfield.occupied:
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
        else:
            print("This field is occupied")
