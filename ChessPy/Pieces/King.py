from Pieces import Piece
from Pieces import Rook


class King(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.canCastle = True
        self.rook1 = None
        self.rook2 = None

    def PossibleMoves(self):
        moves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields

        # checking if the king can move down
        if (col != 0):
            # move down
            if chessboard[8 * (7 - row) + col - 1].occupied == False:
                print("down ", chr(65 + col - 1) + str(row + 1))
                moves += [chr(65 + col - 1) + str(row + 1)]
            else:
                if self.CanCapture(row, col - 1): moves += [chr(65 + col - 1) + str(row + 1)]
            # move down left
            if (row != 0) and (chessboard[8 * (7 - (row - 1)) + col - 1].occupied == False):
                print("down left ", chr(65 + col - 1) + str(row))
                moves += [chr(65 + col - 1) + str(row)]
            else:
                if row != 0 and self.CanCapture(row - 1, col - 1): moves += [chr(65 + col - 1) + str(row)]
            # move down right
            if (row != 7) and chessboard[8 * (7 - (row + 1)) + col - 1].occupied == False:
                print("down right ", chr(65 + col - 1) + str(row + 2))
                moves += [chr(65 + col - 1) + str(row + 2)]
            else:
                if row != 7 and self.CanCapture(row + 1, col - 1): moves += [chr(65 + col - 1) + str(row + 2)]
        #
        # checking if the king can move up
        if (col != 7):
            # move up
            if chessboard[8 * (7 - row) + col + 1].occupied == False:
                print("up ", chr(65 + col + 1) + str(row + 1))
                moves += [chr(65 + col + 1) + str(row + 1)]
            else:
                if self.CanCapture(row, col + 1): moves += [chr(65 + col + 1) + str(row + 1)]
            # move up left
            if (row != 0) and (chessboard[8 * (7 - (row - 1)) + col + 1].occupied == False):
                print("up left", chr(65 + col + 1) + str(row))
                moves += [chr(65 + col + 1) + str(row)]
            else:
                if row != 0 and self.CanCapture(row - 1, col + 1): moves += [chr(65 + col + 1) + str(row)]

            # move up right
            if (row != 7) and chessboard[8 * (7 - (row + 1)) + col + 1].occupied == False:
                print("up right", chr(65 + col + 1) + str(row + 2))
                moves += [chr(65 + col + 1) + str(row + 2)]

            else:
                if row != 7 and self.CanCapture(row + 1, col + 1): moves += [chr(65 + col + 1) + str(row + 2)]

        # checking if the king can move to the right
        if (row != 7) and chessboard[8 * (7 - (row + 1)) + col].occupied == False:
            print("right ", chr(65 + col) + str(row + 2))
            moves += [chr(65 + col) + str(row + 2)]  # moving right
        else:
            if row != 7 and self.CanCapture(row + 1, col): moves += [chr(65 + col) + str(row + 2)]
        # checking if the king can move to the left
        if (row != 0) and chessboard[8 * (7 - (row - 1)) + col].occupied == False:
            moves += [chr(65 + col) + str(row)]  # moving left
        else:
            if row != 0 and self.CanCapture(row - 1, col): moves += [chr(65 + col) + str(row)]

        # checking if the king can castle kingside:
        condition = self.CanCastleKingSide()

        if condition:
            moves += [chr(65 + col + 2) + str(row + 1)]

        # checking if the king can castle quuenside
        condition = self.CanCastleQueenSide()
        if condition:
            moves += [chr(65 + col - 2) + str(row + 1)]

        return moves

    def AttackMoves(self):
        moves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields

        # checking if the king can attack left
        if (col != 0):
            # attack left
            moves += [chr(65 + col - 1) + str(row + 1)]
            # move  left down
            if (row != 0) :
                moves += [chr(65 + col - 1) + str(row)]
            # move left up
            if (row != 7) :
                moves += [chr(65 + col - 1) + str(row + 2)]

        # checking if the king can attack on the right
        if (col != 7):
            # attack right

            moves += [chr(65 + col + 1) + str(row + 1)]

            #attack right down
            if (row != 0):
                moves += [chr(65 + col + 1) + str(row)]

            # move right up
            if (row != 7) :
                moves += [chr(65 + col + 1) + str(row + 2)]

        # checking if the king can attack up
        if (row != 7) :
            moves += [chr(65 + col) + str(row + 2)]  # moving right
        # checking if the king can attack down
        if (row != 0):
            moves += [chr(65 + col) + str(row)]  # moving left
        return moves

    def CanCastleKingSide(self):
        if self.canCastle:
            # print("the king has the atribute on true")
            if self.color == "white":
                # print("white king castling")
                row = self.field.position[0]
                col = self.field.position[1]
                chessboard = self.table
                if chessboard.BoardFields[8 * (7 - (row)) + col + 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col + 2].occupied == False:
                    for whitepiece in chessboard.whitePieces:
                        # print("finding the rook")
                        if isinstance(whitepiece, Rook.Rook) and whitepiece.field.position == (row, col + 3):
                            # print("rook found")
                            if whitepiece.canCastle:
                                self.rook1 = whitepiece
                                return True
        return False

    def CanCastleQueenSide(self):
        if self.canCastle:
            # print("the king has the atribute on true")
            if self.color == "white":
                # print("white king castling")
                row = self.field.position[0]
                col = self.field.position[1]
                chessboard = self.table
                if chessboard.BoardFields[8 * (7 - (row)) + col - 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col - 2].occupied == False:
                    for whitepiece in chessboard.whitePieces:
                        # print("finding the rook")
                        if isinstance(whitepiece, Rook.Rook) and whitepiece.field.position == (row, col - 4):
                            # print("rook found")
                            if whitepiece.canCastle:
                                self.rook2 = whitepiece
                                return True
        return False

    def Move(self, newfield):
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields
        if str(newfield) in self.PossibleMoves():
            # efectuarea rocadei mici
            if (self.field.position[1] + 2 == newfield.position[1]):
                # print(str(chessboard[8*(7-(row))+col+1]))
                self.rook1.Move(self.table.BoardFields[8 * (7 - (row)) + col + 1])
            # efectuarea rocadei mari
            if (self.field.position[1] - 2 == newfield.position[1]):
                # print(str(chessboard[8*(7-(row))+col+1]))
                self.rook2.Move(self.table.BoardFields[8 * (7 - (row)) + col - 1])

            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            self.moved = True
            if self.canCastle == True: self.canCastle = False

        else:
            print("That is not a correct move for the king")

    def __str__(self):
        if self.color == "white": return "♔"
        return "♚"
