from Pieces import Piece


class Rook(Piece.Piece):
    """
    This class implements the chess rook piece behavior
    """

    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.canCastle = True

    def PossibleMoves(self):
        """
        Creates the moving pattern for the queen according to her current position
        :return: list of Field objects
        """
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        # adding the horrizontal possible moves
        # right
        for i in range(col + 1, 8):
            # print(chr(65+i)+str(row+1))
            if chessboard[8 * (7 - (row)) + i].occupied == False:
                # print("camp liber")
                possiblemoves += [chessboard[8 * (7 - (row)) + i]]
            else:
                if self.CanCapture(row, i): possiblemoves += [chessboard[8 * (7 - (row)) + i]]
                break
        # print("left")
        # left
        for i in range(1, col + 1):
            # print(chr(65 +col-i) + str(row + 1))
            if chessboard[8 * (7 - (row)) + col - i].occupied == False:

                # print("camp liber")
                possiblemoves += [chessboard[8 * (7 - (row)) + col - i]]
            else:
                if self.CanCapture(row, col - i): possiblemoves += [chessboard[8 * (7 - (row)) + col - i]]
                break

        # adding the vertical behavior
        # up
        for i in range(row + 1, 8):
            # print(chr(65+col)+str(i+1))

            if chessboard[8 * (7 - i) + col].occupied == False:
                # print("da")
                possiblemoves += [chessboard[8 * (7 - i) + col]]
            else:
                if self.CanCapture(i, col): possiblemoves += [chessboard[8 * (7 - i) + col]]
                break
        # down
        for i in range(1, row + 1):
            # print(chr(65 + col) + str(row - i + 1))
            if chessboard[8 * (7 - (row - i)) + col].occupied == False:
                # print("da")
                possiblemoves += [chessboard[8 * (7 - (row - i)) + col]]
            else:
                if self.CanCapture(row - i, col): possiblemoves += [chessboard[8 * (7 - (row - i)) + col]]
                break
        return possiblemoves

    def AttackMoves(self):
        """
        Creates a list of string representing the attack field where the rook can attack
        :return: list of string objects
        """
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        # adding the horrizontal possible moves
        # right
        for i in range(col + 1, 8):
            # print(chr(65+i)+str(row+1))
            if chessboard[8 * (7 - (row)) + i].occupied == False:
                # print("camp liber")
                possiblemoves += [chr(65 + i) + str(row + 1)]
            else:
                possiblemoves += [chr(65 + i) + str(row + 1)]
                break
        # print("left")
        # left
        for i in range(1, col + 1):
            # print(chr(65 +col-i) + str(row + 1))
            if chessboard[8 * (7 - (row)) + col - i].occupied == False:

                # print("camp liber")
                possiblemoves += [chr(65 + col - i) + str(row + 1)]
            else:
                possiblemoves += [chr(65 + col - i) + str(row + 1)]
                break

        # adding the vertical behavior
        # up
        for i in range(row + 1, 8):
            # print(chr(65+col)+str(i+1))

            if chessboard[8 * (7 - i) + col].occupied == False:
                # print("da")
                possiblemoves += [chr(65 + col) + str(i + 1)]
            else:
                possiblemoves += [chr(65 + col) + str(i + 1)]
                break
        # down
        for i in range(1, row + 1):
            # print(chr(65 + col) + str(row - i + 1))
            if chessboard[8 * (7 - (row - i)) + col].occupied == False:
                # print("da")
                possiblemoves += [chr(65 + col) + str(row - i + 1)]
            else:
                possiblemoves += [chr(65 + col) + str(row - i + 1)]
                break

        return possiblemoves

    def Move(self, newfield, moves):
        """
        Moves the rook to a new field on the chess board
        :param newfield: field where I move the rook to
        :param moves: list of Field objects representing the rook's correct or possible moves
        :return: None
        """
        if newfield in moves:
            if newfield.occupied:
                self.table.RemovePiece(self.table.GetPiece(newfield))
                self.table.noCaptureCount = 0
            else:
                self.table.noCaptureCount += 1
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            self.moved = True
            self.canCastle = False
        else:
            print(self.Warning())

    def Warning(self):
        """
        Returns the warning for making an invalid move for the pawn
        :return: string
        """
        return "That is not a correct move for the rook"

    def Image(self):
        """
        Returns the path to the image for displaying the rook on screen
        :return: string
        """
        if self.color == "white":
            return "Images/tura alba.jpg"
        else:
            return "Images/tura neagra.jpg"

    def __str__(self):
        if self.color == "white": return "♖"
        return "♜"
