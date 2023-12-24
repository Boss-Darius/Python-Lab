from Pieces import Piece
from Pieces import Queen
from Pieces import Rook
from Pieces import Knight
from Pieces import Bishop


class Pawn(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.promoted = False

    def Promote(self):
        if self.promoted == False:
            # let the player choose what piece to promote to
            print("Promote pawn to:")
            print("Queen:  1")
            print("Rook:   2")
            print("Knight: 3")
            print("Bishop: 4")

            promoted = int(input())
            # creating a new piece at the pawn's position
            if promoted == 1: return Queen.Queen(self.table, self.field.position, self.color)
            if promoted == 2: return Rook.Rook(self.table, self.field.position, self.color)
            if promoted == 3: return Knight.Knight(self.table, self.field.position, self.color)
            if promoted == 4: return Bishop.Bishop(self.table, self.field.position, self.color)
            self.promoted == True

    def PossibleMoves(self):

        possibleMoves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields
        # the white pawn can only move up
        if self.color == "white":
            # the pawn hasn't been moved, it can move 2 squares instead of one
            if row == 1 and self.moved == False and (
                    chessboard[8 * (7 - row - 1) + col].occupied == False and chessboard[
                8 * (7 - row - 2) + col].occupied == False):
                possibleMoves += [chr(65 + col) + str(row + 3)]

            if (row != 7) and (chessboard[8 * (7 - row - 1) + col].occupied == False):
                possibleMoves += [chr(65 + col) + str(row + 2)]
                # capture on left
                if col != 0 and chessboard[8 * (7 - (row + 1)) + col - 1].occupied and self.CanCapture(row + 1,
                                                                                                       col - 1):
                    possibleMoves += [chr(65 + col - 1) + str(row + 2)]
                # capture on right
                if col != 7 and chessboard[8 * (7 - (row + 1)) + col + 1].occupied and self.CanCapture(row + 1,
                                                                                                       col + 1):
                    possibleMoves += [chr(65 + col + 1) + str(row + 2)]
        # the blackPawn can only move down
        else:
            if row == 6 and self.moved == False:
                possibleMoves += [chr(65 + col) + str(row - 1)]
            if row != 0:
                possibleMoves += [chr(65 + col) + str(row)]
                # capture on left
                if col != 0 and chessboard[8 * (7 - (row - 1)) + col - 1].occupied and self.CanCapture(row - 1,
                                                                                                       col - 1):
                    possibleMoves += [chr(65 + col - 1) + str(row)]
                # capture on right
                if col != 7 and chessboard[8 * (7 - (row - 1)) + col + 1].occupied and self.CanCapture(row - 1,
                                                                                                       col + 1):
                    possibleMoves += [chr(65 + col + 1) + str(row)]

        return possibleMoves

    def AttackMoves(self):
        attackMoves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields

        # attack possibilities for the white pawn
        if self.color == "white":
            if row != 7 and col != 0 and chessboard[8 * (7 - (row + 1)) + col - 1].occupied and self.CanCapture(row + 1,
                                                                                                                col - 1):
                attackMoves += [chr(65 + col - 1) + str(row + 2)]
            # capture on right
            if row != 7 and col != 7 and chessboard[8 * (7 - (row + 1)) + col + 1].occupied and self.CanCapture(row + 1,
                                                                                                                col + 1):
                attackMoves += [chr(65 + col + 1) + str(row + 2)]

        # attack posibilities for the black pawn
        else:
            if col != 0 and chessboard[8 * (7 - (row - 1)) + col - 1].occupied and self.CanCapture(row - 1, col - 1):
                attackMoves += [chr(65 + col - 1) + str(row)]
            # capture on right
            if col != 7 and chessboard[8 * (7 - (row - 1)) + col + 1].occupied and self.CanCapture(row - 1, col + 1):
                attackMoves += [chr(65 + col + 1) + str(row)]

        return attackMoves

    def Move(self, newfield):
        if str(newfield) in self.PossibleMoves():
            print("attack moves: ", self.AttackMoves())
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            # checking if the pawn got to the promotong state
            # promoting the white pawn
            if newfield.position[0] == 7 and self.color == "white":
                self = self.Promote()
                self.table.RemovePiece(self)
            # promoting the black pawn
            if newfield.position[0] == 0 and self.color == "black":
                self.Promote()
                # deleting the pawn
                self.table.RemovePiece(self)
        else:
            print("that is not a correct move dor the pawn")

    def __str__(self):
        if self.color == "white": return "♙"
        return "♟"

    def __del__(self):
        self.field.ChangeStatus()
        if self.color == "white":
            self.table.whitePieces.remove(self)
        else:
            self.table.blackPieces.remove(self)

        print("am ajuns pana aici")
