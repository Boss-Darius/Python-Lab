from Pieces import Piece
from Pieces import Rook
import copy

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

    def Image(self):
        if self.color == "white":
            return "Images/rege alb2.png"
        else:
            return "Images/rege negru2.png"

    def PossibleMoves(self):
        moves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields

        # checking if the king can move down
        if (col != 0):
            # move down
            if chessboard[8 * (7 - row) + col - 1].occupied == False:
                # print("down ", chr(65 + col - 1) + str(row + 1))
                moves += [chessboard[8 * (7 - row) + col - 1]]
            else:
                if self.CanCapture(row, col - 1): moves += [chessboard[8 * (7 - row) + col - 1]]
            # move down left
            if (row != 0) and (chessboard[8 * (7 - (row - 1)) + col - 1].occupied == False):
                # print("down left ", chr(65 + col - 1) + str(row))
                moves += [chessboard[8 * (7 - (row - 1)) + col - 1]]
            else:
                if row != 0 and self.CanCapture(row - 1, col - 1): moves += [chessboard[8 * (7 - (row - 1)) + col - 1]]
            # move down right
            if (row != 7) and chessboard[8 * (7 - (row + 1)) + col - 1].occupied == False:
                # print("down right ", chr(65 + col - 1) + str(row + 2))
                moves += [chessboard[8 * (7 - (row + 1)) + col - 1]]
            else:
                if row != 7 and self.CanCapture(row + 1, col - 1): moves += [chessboard[8 * (7 - (row + 1)) + col - 1]]
        #
        # checking if the king can move up
        if (col != 7):
            # move up
            if chessboard[8 * (7 - row) + col + 1].occupied == False:
                # print("up ", chr(65 + col + 1) + str(row + 1))
                moves += [chessboard[8 * (7 - row) + col + 1]]
            else:
                if self.CanCapture(row, col + 1): moves += [chessboard[8 * (7 - row) + col + 1]]
            # move up left
            if (row != 0) and (chessboard[8 * (7 - (row - 1)) + col + 1].occupied == False):
                # print("up left", chr(65 + col + 1) + str(row))
                moves += [chessboard[8 * (7 - (row - 1)) + col + 1]]
            else:
                if row != 0 and self.CanCapture(row - 1, col + 1): moves += [chessboard[8 * (7 - (row - 1)) + col + 1]]

            # move up right
            if (row != 7) and chessboard[8 * (7 - (row + 1)) + col + 1].occupied == False:
                # print("up right", chr(65 + col + 1) + str(row + 2))
                moves += [chessboard[8 * (7 - (row + 1)) + col + 1]]

            else:
                if row != 7 and self.CanCapture(row + 1, col + 1): moves += [chessboard[8 * (7 - (row + 1)) + col + 1]]

        # checking if the king can move to the right
        if (row != 7) and chessboard[8 * (7 - (row + 1)) + col].occupied == False:
            # print("right ", chr(65 + col) + str(row + 2))
            moves += [chessboard[8 * (7 - (row + 1)) + col]]  # moving right
        else:
            if row != 7 and self.CanCapture(row + 1, col): moves += [chessboard[8 * (7 - (row + 1)) + col]]
        # checking if the king can move to the left
        if (row != 0) and chessboard[8 * (7 - (row - 1)) + col].occupied == False:
            moves += [chessboard[8 * (7 - (row - 1)) + col]]  # moving left
        else:
            if row != 0 and self.CanCapture(row - 1, col): moves += [chessboard[8 * (7 - (row - 1)) + col]]

        # checking if the king can castle kingside:
        condition = self.CanCastleKingSide()

        if condition:
            moves += [chessboard[8 * (7 - (row)) + col + 2]]  #

        # checking if the king can castle quuenside
        condition = self.CanCastleQueenSide()
        if condition:
            moves += [chessboard[8 * (7 - (row)) + col - 2]]

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
            if (row != 0):
                moves += [chr(65 + col - 1) + str(row)]
            # move left up
            if (row != 7):
                moves += [chr(65 + col - 1) + str(row + 2)]

        # checking if the king can attack on the right
        if (col != 7):
            # attack right

            moves += [chr(65 + col + 1) + str(row + 1)]

            # attack right down
            if (row != 0):
                moves += [chr(65 + col + 1) + str(row)]

            # move right up
            if (row != 7):
                moves += [chr(65 + col + 1) + str(row + 2)]

        # checking if the king can attack up
        if (row != 7):
            moves += [chr(65 + col) + str(row + 2)]  # moving right
        # checking if the king can attack down
        if (row != 0):
            moves += [chr(65 + col) + str(row)]  # moving left
        return moves

    def CanCastleKingSide(self):
        if self.canCastle and not self.InCheck():
            row = self.field.position[0]
            col = self.field.position[1]
            chessboard = self.table
            # print("the king has the atribute on true")
            if self.color == "white":
                # print("white king castling")
                if chessboard.BoardFields[8 * (7 - (row)) + col + 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col + 2].occupied == False:
                    for whitepiece in chessboard.whitePieces:
                        # print("finding the rook")
                        if isinstance(whitepiece, Rook.Rook) and whitepiece.field.position == (row, col + 3):
                            # print("rook found")
                            if whitepiece.canCastle:
                                self.rook1 = whitepiece
                                return True
            else:
                if chessboard.BoardFields[8 * (7 - (row)) + col + 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col + 2].occupied == False:
                    print("fields clear")
                    for blackpiece in chessboard.blackPieces:
                        print("finding the rook")
                        if isinstance(blackpiece, Rook.Rook) and blackpiece.field.position == (row, col + 3):
                            print("rook found")
                            if blackpiece.canCastle:
                                self.rook1 = blackpiece
                                return True
        return False

    def CanCastleQueenSide(self):
        if self.canCastle and not self.InCheck():
            row = self.field.position[0]
            col = self.field.position[1]
            chessboard = self.table
            # print("the king has the atribute on true")
            if self.color == "white":
                # print("white king castling")
                if chessboard.BoardFields[8 * (7 - (row)) + col - 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col - 2].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col - 3].occupied == False:
                    for whitepiece in chessboard.whitePieces:
                        # print("finding the rook")
                        if isinstance(whitepiece, Rook.Rook) and whitepiece.field.position == (row, col - 4):
                            # print("rook found")
                            if whitepiece.canCastle:
                                self.rook2 = whitepiece
                                return True
            else:
                if chessboard.BoardFields[8 * (7 - (row)) + col - 1].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col - 2].occupied == False and chessboard.BoardFields[
                    8 * (7 - (row)) + col - 3].occupied == False:
                    for blackpiece in chessboard.blackPieces:
                        # print("finding the rook")
                        if isinstance(blackpiece, Rook.Rook) and blackpiece.field.position == (row, col - 4):
                            # print("rook found")
                            if blackpiece.canCastle:
                                self.rook2 = blackpiece
                                return True

        return False

    def InCheck(self):
        enemyPieces = []
        enemyAttackMoves = []
        if self.color == "white":
            enemyPieces = self.table.blackPieces
        else:
            enemyPieces = self.table.whitePieces

        for piece in enemyPieces:
            for attack in piece.AttackMoves():
                enemyAttackMoves += [attack]
        if str(self.field) in enemyAttackMoves: return True
        return False

    def Move(self, newfield, moves):
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields
        if newfield in moves:
            # efectuarea rocadei mici
            if (self.field.position[1] + 2 == newfield.position[1]):
                # print(str(chessboard[8*(7-(row))+col+1]))
                self.rook1.Move(self.table.BoardFields[8 * (7 - (row)) + col + 1], self.rook1.FilterMoves())
            # efectuarea rocadei mari
            if (self.field.position[1] - 2 == newfield.position[1]):
                # print(str(chessboard[8*(7-(row))+col+1]))
                self.rook2.Move(self.table.BoardFields[8 * (7 - (row)) + col - 1], self.rook2.PossibleMoves())
                # self.rook2.field.ChangeStatus()
                # self.rook2.field=self.table.BoardFields[8 * (7 - (row)) + col - 1]
                # self.rook2.field.ChangeStatus()

            if newfield.occupied:
                self.table.RemovePiece(self.table.GetPiece(newfield))
                self.table.noCaptureCount = 0
            else:
                self.table.noCaptureCount += 1

            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            self.moved = True
            if self.canCastle == True: self.canCastle = False

        else:
            print(self.Warning())

    def Warning(self):
        return "That is not a correct move for the King"

    def __str__(self):
        if self.color == "white": return "♔"
        return "♚"
