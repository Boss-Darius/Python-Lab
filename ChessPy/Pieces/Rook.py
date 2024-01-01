from Pieces import Piece


class Rook(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.canCastle = True

    def PossibleMoves(self):
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

    def Move(self, newfield,moves):
        if newfield in moves:
            if newfield.occupied:
                self.table.RemovePiece(self.table.GetPiece(newfield))
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            self.moved = True
            self.canCastle = False
        else:
            print(self.Warning())

    def Warning(self):
        return "That is not a correct move for the rook"

    def __str__(self):
        if self.color == "white": return "♖"
        return "♜"
