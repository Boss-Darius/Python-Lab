import Pieces.King
import copy
from Field import Field
import copy


class Piece:
    """
        Base class for the classes that implement chess pieces
    """

    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PrintPosition(self):
        """ Shows the representation of the piece's field as the chess board notation
            :return: string
        """
        return self.field.PrintPosition()

    def AttackMoves(self):
        """ Takes the string representation of the fields where the piece can attack other pieces
            Function to be overriden by other classes
            :return: None
        """
        return None

    def CanCapture(self, row, col):
        """
        Checks if the piece can capture the piece on the field at the specific row and column
        :param row: row of the piece I check if I can capture
        :param col: col of the piece I check if I can capture
        :return: True if the piece can be captured , False otherwise
        """
        chessboard = self.table.BoardFields
        if (self.color == "white" and chessboard[8 * (7 - (row)) + col] in self.table.BlackPiecesFields()):
            # print("capture for white")
            # we can't capture the kings
            if not (isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col]), Pieces.King.King)): return True
        elif (self.color == "black" and chessboard[8 * (7 - (row)) + col] in self.table.WhitePiecesFields()):
            # print("capture for black")
            # we can't capture the kings
            if not (isinstance(self.table.GetPiece(chessboard[8 * (7 - (row)) + col]), Pieces.King.King)): return True
        else:
            # print("not capturing")
            return False

    def ShowPossibleMoves(self):
        """ Creates a better way to visualize the moves a piece can do according to its moving pattern
            :return: list of string objects
        """
        possibleMoves = []
        for possibleMove in self.PossibleMoves():
            possibleMoves += [str(possibleMove)]

        # print(possibleMoves)
        return possibleMoves

    def FilterMoves(self):
        """ Validates the moves a piece can make according to its moving pattern
            :return: list of Field objects
        """

        movesList = self.PossibleMoves()
        filteredMoves = []
        originalRow, originalCol = self.field.position
        for move in movesList:
            itermediateState = copy.deepcopy(self.table)
            # print("stare curenta")
            # print(itermediateState)
            # print("am aratat starea curenta")
            # print()

            myKing = None
            if self.color == "white":
                for piece in itermediateState.whitePieces:
                    if isinstance(piece, Pieces.King.King):
                        myKing = piece
                        break
            else:
                for piece in itermediateState.blackPieces:
                    if isinstance(piece, Pieces.King.King):
                        myKing = piece
                        break

            row = move.position[0]
            col = move.position[1]

            pieceIMove = itermediateState.GetPiece(itermediateState.BoardFields[8 * (7 - (originalRow)) + originalCol])
            # print(pieceIMove)
            pieceIMove.Move(itermediateState.BoardFields[8 * (7 - (row)) + col], pieceIMove.PossibleMoves())

            # print("stare intermediara")
            # print(itermediateState)
            # print("am aratat starea intermediara")
            if not myKing.InCheck():
                filteredMoves += [move]
                # print(move," mutare valida")
            # else: print(move," mutare invalida")
        return filteredMoves

    def ShowFilteredMoves(self):
        """ Creates a better way to visualize the correct moves a piece can make
            :return: list of string objects
        """
        filteredMoves = []
        for filteredMove in self.FilterMoves():
            filteredMoves += [str(filteredMove)]

        # print(filteredMoves)
        return filteredMoves

    def Warning(self):
        """ Creates a warning for moving the piece on an invalid field
            Function to be overriden by other classes
            :return: string
        """
        return "That is not a correct move for this piece"

    def Move(self, newfield, moves):
        """
        Moves the piece to a field from a list of Field objects

        :param newfield: field I move the piece to
        :param moves: list of Field objects representing the piece's correct or possible moves
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

        else:
            print(self.Warning())
