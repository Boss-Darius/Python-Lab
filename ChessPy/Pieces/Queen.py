from Pieces import Piece


class Queen(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    """ Creates the moving pattern for the queen according to her current position
        Returns a list of Field objects
    """

    def PossibleMoves(self):
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields
        # adding the rook-like behavior
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
        # adding the bishop-like behavior

        if row != 0:
            r1 = row - 1
            c1 = col - 1
            # down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    c1 -= 1
                    r1 -= 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    break

            r1 = row - 1
            c1 = col + 1
            # down right
            while r1 >= 0 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    c1 += 1
                    r1 -= 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    break
            # checking if the bishop can move up
        if row != 7:
            r1 = row + 1
            c1 = col - 1
            # up left
            while r1 <= 7 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    c1 -= 1
                    r1 += 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    break

            r1 = row + 1
            c1 = col + 1
            # up right
            while r1 <= 7 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    c1 += 1
                    r1 += 1
                else:
                    if self.CanCapture(r1, c1): possiblemoves += [chessboard[8 * (7 - r1) + c1]]
                    break
        return possiblemoves

    """ Takes the string representation of the field where the queen can attack other pieces
        Returns a list of string objects
    """

    def AttackMoves(self):
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields

        # rook behavior
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
        # bishop behavior

        if row != 0:
            r1 = row - 1
            c1 = col - 1
            # down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 -= 1
                    r1 -= 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break

            r1 = row - 1
            c1 = col + 1
            # down right
            while r1 >= 0 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 += 1
                    r1 -= 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break
                # checking if the bishop can move up
        if row != 7:
            r1 = row + 1
            c1 = col - 1
            # up left
            while r1 <= 7 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 -= 1
                    r1 += 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break

            r1 = row + 1
            c1 = col + 1
            # up right
            while r1 <= 7 and c1 <= 7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    # print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 += 1
                    r1 += 1
                else:
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    break
        return possiblemoves

    def Warning(self):
        return "That is not a correct move for the queen"

    """ Shows the path to the image for the queen display oin the GUI
        Returns a string
    """

    def Image(self):
        if self.color == "white":
            return "Images/regina alba2.png"
        else:
            return "Images/regina neagra.png"

    def __str__(self):
        if self.color == "white": return "♕"
        return "♛"
