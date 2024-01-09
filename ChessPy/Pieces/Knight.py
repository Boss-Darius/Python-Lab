from Pieces import Piece
from Field import Field


class Knight(Piece.Piece):
    """
    this class implements the chess knight piece behavior
    """

    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PossibleMoves(self):
        """
        Creates the moving pattern for the knight according to its position
        :return: list of Field objects
        """
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
                possiblemoves += [chessboard[8 * (7 - (row + 1)) + col - 2]]
            else:
                # print("capture path left up")
                # capture the piece that is on that field
                if row != 7 and self.CanCapture(row + 1, col - 2): possiblemoves += [
                    chessboard[8 * (7 - (row + 1)) + col - 2]]
            # left down
            if row != 0 and chessboard[8 * (7 - (row - 1)) + col - 2].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row - 1)) + col - 2]]

            else:
                # print("capture path left down")
                # capture the piece that is on that field
                if row != 0 and self.CanCapture(row - 1, col - 2): possiblemoves += [
                    chessboard[8 * (7 - (row - 1)) + col - 2]]

        # checking if the knight can move to the right

        if col < 6:
            # right up
            if row != 7 and chessboard[8 * (7 - (row + 1)) + col + 2].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row + 1)) + col + 2]]

            else:
                # capture the piece that is on that field
                if row != 7 and self.CanCapture(row + 1, col + 2): possiblemoves += [
                    chessboard[8 * (7 - (row + 1)) + col + 2]]
            # right down
            if row != 0 and chessboard[8 * (7 - (row - 1)) + col + 2].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row - 1)) + col + 2]]
            else:
                # capture the piece that is on that field
                if row != 0 and self.CanCapture(row - 1, col + 2): possiblemoves += [
                    chessboard[8 * (7 - (row - 1)) + col + 2]]

        # checking if the knight can move up

        if row > 1:
            # up left
            if col != 0 and chessboard[8 * (7 - (row - 2)) + col - 1].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row - 2)) + col - 1]]
            else:
                # print("capture path up left")
                # capture the piece that is on that field
                if col != 0 and self.CanCapture(row - 2, col - 1): possiblemoves += [
                    chessboard[8 * (7 - (row - 2)) + col - 1]]
            # up right
            if col != 7 and chessboard[8 * (7 - (row - 2)) + col + 1].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row - 2)) + col + 1]]
            else:
                # print("capture path up right")
                # capture the piece that is on that field
                if col != 7 and self.CanCapture(row - 2, col + 1): possiblemoves += [
                    chessboard[8 * (7 - (row - 2)) + col + 1]]

        # cheking if the knight can move down
        if row < 6:
            # down left
            if col != 0 and chessboard[8 * (7 - (row + 2)) + col - 1].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row + 2)) + col - 1]]
            else:
                # print("capture path down left")
                # capture the piece that is on that field
                if col != 0 and self.CanCapture(row + 2, col - 1): possiblemoves += [
                    chessboard[8 * (7 - (row + 2)) + col - 1]]

            # down right
            if col != 7 and chessboard[8 * (7 - (row + 2)) + col + 1].occupied == False:
                possiblemoves += [chessboard[8 * (7 - (row + 2)) + col + 1]]
            else:
                # print("capture path down right")
                # capture the piece that is on that field
                # print(chessboard[8 * (7 - (row + 2)) + col + 1], ' ', self.CanCapture(row + 2, col + 1))
                if col != 7 and self.CanCapture(row + 2, col + 1): possiblemoves += [
                    chessboard[8 * (7 - (row + 2)) + col + 1]]

        return possiblemoves

    def Warning(self):
        """
        Creates the warning for making an invalid move for the knight
        :return:
        """
        return "That is not a correct move for the knight"

    def Image(self):
        """
        Returns the path of the image used to display the knight on screen
        :return:
        """
        if self.color == "white":
            return "Images/cal alb.jpg"
        else:
            return "Images/cal negru.jpg"

    def AttackMoves(self):
        """
        Creates a list of strings representing the fields where the knight can attack other pieces
        :return: list of string objects
        """
        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        attackmoves = []

        # checking if the knight can move to the left

        if col > 1:
            if row != 7:
                attackmoves += [chr(65 + col - 2) + str(row + 2)]

            # left down
            if row != 0:
                attackmoves += [chr(65 + col - 2) + str(row)]

        # checking if the knight can move to the right

        if col < 6:
            # right up
            if row != 7:
                attackmoves += [chr(65 + col + 2) + str(row + 2)]

            # right down
            if row != 0:
                attackmoves += [chr(65 + col + 2) + str(row)]

        # checking if the knight can move up

        if row > 1:
            # up left
            if col != 0:
                attackmoves += [chr(65 + col - 1) + str(row - 1)]

            # up right
            if col != 7:
                attackmoves += [chr(65 + col + 1) + str(row - 1)]

        # cheking if the knight can move down
        if row < 6:
            # down left
            if col != 0:
                attackmoves += [chr(65 + col - 1) + str(row + 3)]

            # down right
            if col != 7:
                attackmoves += [chr(65 + col + 1) + str(row + 3)]

        return attackmoves

    def __str__(self):
        if self.color == "white": return "♘"
        return "♞"
