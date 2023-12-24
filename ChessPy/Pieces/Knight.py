from Pieces import Piece
from Field import Field


class Knight(Piece.Piece):

    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PossibleMoves(self):
        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        possiblemoves = []

        # checking if the knight can move to the left

        if col > 1:
            # left up
            # --
            # |
            if row != 7 and chessboard[8 * (7 - (row + 1)) + col - 2].occupied == False:
                possiblemoves += [chr(65 + col - 2) + str(row + 2)]
            else:
                print("capture path left up")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row + 1)) + col - 2], ' ', self.CanCapture(row + 1, col - 2))
                if self.CanCapture(row + 1, col - 2): possiblemoves += [chr(65 + col - 2) + str(row + 2)]
            # left down
            if row != 0 and chessboard[8 * (7 - (row - 1)) + col - 2].occupied == False:
                possiblemoves += [chr(65 + col - 2) + str(row)]

            else:
                print("capture path left down")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row - 1)) + col - 2], ' ', self.CanCapture(row - 1, col - 2))
                if self.CanCapture(row - 1, col - 2): possiblemoves += [chr(65 + col - 2) + str(row)]

        # checking if the knight can move to the right

        if col < 6:
            # right up
            if row != 7 and chessboard[8 * (7 - (row + 1)) + col + 2].occupied == False:
                possiblemoves += [chr(65 + col + 2) + str(row + 2)]

            else:
                print("capture path right up")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row + 1)) + col + 2], ' ', self.CanCapture(row + 1, col + 2))
                # capture
                if self.CanCapture(row + 1, col + 2): possiblemoves += [chr(65 + col + 2) + str(row + 2)]
            # right down
            if row != 0 and chessboard[8 * (7 - (row - 1)) + col + 2].occupied == False:
                possiblemoves += [chr(65 + col + 2) + str(row)]
            else:
                print("capture path right down")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row - 1)) + col + 2], ' ', self.CanCapture(row - 1, col + 2))
                if self.CanCapture(row - 1, col + 2): possiblemoves += [chr(65 + col + 2) + str(row)]

        # checking if the knight can move up

        if row > 1:
            # up left
            if col != 0 and chessboard[8 * (7 - (row - 2)) + col - 1].occupied == False:
                possiblemoves += [chr(65 + col - 1) + str(row - 1)]
            else:
                print("capture path up left")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row - 2)) + col - 1], ' ', self.CanCapture(row - 2, col - 1))
                if self.CanCapture(row - 2, col - 1): possiblemoves += [chr(65 + col - 1) + str(row - 1)]
            # up right
            if col != 7 and chessboard[8 * (7 - (row - 2)) + col + 1].occupied == False:
                possiblemoves += [chr(65 + col + 1) + str(row - 1)]
            else:
                print("capture path up right")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row - 2)) + col + 1], ' ', self.CanCapture(row - 2, col + 1))
                if self.CanCapture(row - 2, col + 1): possiblemoves += [chr(65 + col + 1) + str(row - 1)]

        # cheking if the knight can move down
        if row < 6:
            # down left
            if col != 0 and chessboard[8 * (7 - (row + 2)) + col - 1].occupied == False:
                possiblemoves += [chr(65 + col - 1) + str(row + 3)]
            else:
                print("capture path down left")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row + 2)) + col - 1], ' ', self.CanCapture(row + 2, col - 1))
                if self.CanCapture(row + 2, col - 1): possiblemoves += [chr(65 + col - 1) + str(row + 3)]

            # down right
            if col != 7 and chessboard[8 * (7 - (row + 2)) + col + 1].occupied == False:
                possiblemoves += [chr(65 + col + 1) + str(row + 3)]
            else:
                print("capture path down right")
                # capture the piece that is on that field
                print(chessboard[8 * (7 - (row + 2)) + col + 1], ' ', self.CanCapture(row + 2, col + 1))
                if self.CanCapture(row + 2, col + 1): possiblemoves += [chr(65 + col + 1) + str(row + 3)]

        return possiblemoves

    def Move(self, newfield):
        if str(newfield) in self.PossibleMoves():
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
        else:
            print("That is not a correct move for the knight")

    def __str__(self):
        if self.color == "white": return "♘"
        return "♞"
