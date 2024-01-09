from Pieces import Piece
import copy


class Pawn(Piece.Piece):
    """
    This class implements the pawn's behavior
    """

    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.promoted = False
        self.Enpassant = False

    def Promote(self):
        """ Sets the promoted field of the pawn to True
            :return: None
        """
        if self.promoted == False:
            self.promoted = True

    def PossibleMoves(self):
        """ Creates the moving pattern for the pawn according to its current position
             :return: list
         """
        possibleMoves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields
        # the white pawn can only move up
        if self.color == "white":
            # the pawn hasn't been moved, it can move 2 squares instead of one
            if row == 1 and self.moved == False and (
                    chessboard[8 * (7 - (row + 1)) + col].occupied == False and chessboard[
                8 * (7 - row - 2) + col].occupied == False):
                possibleMoves += [chessboard[8 * (7 - (row + 2)) + col]]

            if (row != 7) and (chessboard[8 * (7 - (row + 1)) + col].occupied == False):
                possibleMoves += [chessboard[8 * (7 - (row + 1)) + col]]
                # capture on left
            if row != 7 and col != 0 and chessboard[8 * (7 - (row + 1)) + col - 1].occupied and self.CanCapture(row + 1,
                                                                                                                col - 1):
                possibleMoves += [chessboard[8 * (7 - (row + 1)) + col - 1]]
            # capture on right
            if row != 7 and col != 7 and chessboard[8 * (7 - (row + 1)) + col + 1].occupied and self.CanCapture(row + 1,
                                                                                                                col + 1):
                possibleMoves += [chessboard[8 * (7 - (row + 1)) + col + 1]]
            # cheking if the pawn can Enpassant other pawns

            if col != 7:
                if isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col + 1]),
                              Pawn) and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col + 1]).color != "white" and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col + 1]).Enpassant:
                    possibleMoves += [chessboard[8 * (7 - (row + 1)) + col + 1]]

            if col != 0:
                if isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col - 1]),
                              Pawn) and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col - 1]).color != "white" and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col - 1]).Enpassant:
                    possibleMoves += [chessboard[8 * (7 - (row + 1)) + col - 1]]

        # the blackPawn can only move down
        else:
            if row == 6 and self.moved == False and (
                    chessboard[8 * (7 - (row - 1)) + col].occupied == False and chessboard[
                8 * (7 - (row - 2)) + col].occupied == False):
                possibleMoves += [chessboard[8 * (7 - (row - 2)) + col]]
            if row != 0:
                if chessboard[8 * (7 - (row - 1)) + col].occupied == False:
                    possibleMoves += [chessboard[8 * (7 - (row - 1)) + col]]
                # capture on left
                if col != 0 and chessboard[8 * (7 - (row - 1)) + col - 1].occupied and self.CanCapture(row - 1,
                                                                                                       col - 1):
                    possibleMoves += [chessboard[8 * (7 - (row - 1)) + col - 1]]
                # capture on right
                if col != 7 and chessboard[8 * (7 - (row - 1)) + col + 1].occupied and self.CanCapture(row - 1,
                                                                                                       col + 1):
                    possibleMoves += [chessboard[8 * (7 - (row - 1)) + col + 1]]
            # cheking if the pawn can Enpassant other pawns

            if col != 7:
                if isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col + 1]),
                              Pawn) and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col + 1]).color != "black" and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col + 1]).Enpassant:
                    possibleMoves += [chessboard[8 * (7 - (row - 1)) + col + 1]]

            if col != 0:
                if isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col - 1]),
                              Pawn) and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col - 1]).color != "black" and self.table.GetPiece(
                    chessboard[8 * (7 - (row)) + col - 1]).Enpassant:
                    possibleMoves += [chessboard[8 * (7 - (row - 1)) + col - 1]]

        return possibleMoves

    def Warning(self):
        """ Creates a warning indicating that the move is not correct for the pawn
            :return: string
        """
        return "That is not a correct move for this pawn"

    def Image(self):
        """ Shows the path to the image for pawn display on the GUI
            :return: string
        """
        if self.color == "white":
            return "Images/pion alb.jpg"
        else:
            return "Images/pion negru.jpg"

    def AttackMoves(self):
        """ Takes the string representation of fields where the pawn can attack other pieces
            :return:  list
        """
        attackMoves = []
        row = self.field.position[0]
        col = self.field.position[1]
        chessboard = self.table.BoardFields

        # attack possibilities for the white pawn
        if self.color == "white":
            if row != 7 and col != 0:
                attackMoves += [chr(65 + col - 1) + str(row + 2)]
            # capture on right
            if row != 7 and col != 7:
                attackMoves += [chr(65 + col + 1) + str(row + 2)]

        # attack posibilities for the black pawn
        else:
            if col != 0 and row != 0:
                attackMoves += [chr(65 + col - 1) + str(row)]
            # capture on right
            if col != 7 and row != 0:
                attackMoves += [chr(65 + col + 1) + str(row)]

        return attackMoves

    def Move(self, newfield, moves):
        """
        Moves the pawn to a field from a list of Field objects

        :param newfield: field I move the pawn to
        :param moves: list of Field objects representing the pawn's correct or possible moves
        :return: None
        """
        if newfield in moves:

            # check if the pawn does the double fields move

            if (self.color == "white" and self.field.position[0] + 2 == newfield.position[
                0]) or self.color == "black" and self.field.position[0] - 2 == newfield.position[0]:
                self.Enpassant = True

            elif self.Enpassant == True:
                self.Enpassant = False
            # checking if the pawn can use the enpassant move on other pawns:
            # for the white pawn
            if self.color == "white":

                if newfield.position[0] == self.field.position[0] + 1 and newfield.position[1] == self.field.position[
                    1] + 1:
                    piece = self.table.GetPiece(
                        self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] + 1])
                    if isinstance(piece, Pawn) and piece.color == "black" and piece.Enpassant:
                        self.table.RemovePiece(self.table.GetPiece(
                            self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] + 1]))
                elif newfield.position[0] == self.field.position[0] + 1 and newfield.position[1] == self.field.position[
                    1] - 1:
                    piece = self.table.GetPiece(
                        self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] - 1])
                    if isinstance(piece, Pawn) and piece.color == "black" and piece.Enpassant:
                        self.table.RemovePiece(self.table.GetPiece(
                            self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] - 1]))
            # for the black pawn
            else:
                if newfield.position[0] == self.field.position[0] - 1 and newfield.position[1] == self.field.position[
                    1] + 1:
                    piece = self.table.GetPiece(
                        self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] + 1])
                    if isinstance(piece, Pawn) and piece.color == "black" and piece.Enpassant:
                        self.table.RemovePiece(self.table.GetPiece(
                            self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] + 1]))
                elif newfield.position[0] == self.field.position[0] - 1 and newfield.position[1] == self.field.position[
                    1] - 1:
                    piece = self.table.GetPiece(
                        self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] - 1])
                    if isinstance(piece, Pawn) and piece.color == "black" and piece.Enpassant:
                        self.table.RemovePiece(self.table.GetPiece(
                            self.table.BoardFields[8 * (7 - (self.field.position[0])) + self.field.position[1] - 1]))

            # print(self, " can be ennpassanted : ", self.Enpassant)
            if newfield.occupied and str(newfield) in self.AttackMoves():
                self.table.RemovePiece(self.table.GetPiece(newfield))
                self.table.noCaptureCount = 0
            else:
                self.table.noCaptureCount += 1
            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            # checking if the pawn got to the promoting state
            # promoting the white pawn

            if newfield.position[0] == 7 and self.color == "white":
                self.Promote()
                # self.table.RemovePiece(self)
            # promoting the black pawn
            if newfield.position[0] == 0 and self.color == "black":
                self.Promote()
            #     # deleting the pawn
            #     self.table.RemovePiece(self)
        else:
            print(self.Warning())

    def __str__(self):
        if self.color == "white": return "♙"
        return "♟"
