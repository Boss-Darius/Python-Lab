from Field import Field
import Pieces
from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen
import copy


class Board:
    def __init__(self, whitePieces, blackPieces):
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces
        self.BoardFields = []
        self.noCaptureCount = 0

        for i in range(0, 8):
            for j in range(0, 8):
                self.BoardFields += [Field.BoardField((7 - i, j))]

    def __init__(self):
        self.whitePieces = []
        self.blackPieces = []
        self.BoardFields = []
        self.noCaptureCount = 0

        for i in range(0, 8):
            for j in range(0, 8):
                self.BoardFields += [Field.BoardField((7 - i, j))]
        # adding the kings
        King.King(self, (0, 4), "white")
        King.King(self, (7, 4), "black")

        # adding the queens
        Queen.Queen(self, (0, 3), "white")
        Queen.Queen(self, (7, 3), "black")

        # adding the rooks

        Rook.Rook(self, (0, 0), "white")
        Rook.Rook(self, (0, 7), "white")
        Rook.Rook(self, (7, 0), "black")
        Rook.Rook(self, (7, 7), "black")

        # adding the bishops
        Bishop.Bishop(self, (0, 2), "white")
        Bishop.Bishop(self, (0, 5), "white")
        Bishop.Bishop(self, (7, 2), "black")
        Bishop.Bishop(self, (7, 5), "black")

        # adding the knights
        Knight.Knight(self, (0, 1), "white")
        Knight.Knight(self, (0, 6), "white")
        Knight.Knight(self, (7, 1), "black")
        Knight.Knight(self, (7, 6), "black")

        # adding the pawns

        for i in range(0, 8):
            Pawn.Pawn(self, (1, i), "white")
            Pawn.Pawn(self, (6, i), "black")

    def AddPiece(self, piece):
        if piece.color == "white":
            self.whitePieces += [piece]
        else:
            self.blackPieces += [piece]

    def RemovePiece(self, piece):
        if piece in self.whitePieces:
            piece.field.ChangeStatus()
            self.whitePieces.remove(piece)
        else:
            piece.field.ChangeStatus()
            self.blackPieces.remove(piece)

    # functie de debug
    # verific daca se modifica pozitia pieselor albe pe tabla
    def CheckWhitePiecesFields(self):
        print(self.whitePieces)
        for i in range(0, len(self.whitePieces)):
            print(self.whitePieces[i], ' ', self.whitePieces[i].field.occupied)

    # functie de debug
    # verific ca nu cumva o piesa sa mentina un camp ocupat dupa ce a parasit acel camp
    def OccupiedField(self):
        fieldstring = ""
        for i in range(0, 8):
            for j in range(0, 8):
                if self.BoardFields[(7 - i) * 8 + j].occupied == True:
                    fieldstring += str(self.BoardFields[(7 - i) * 8 + j]) + " "

        return fieldstring

    def GetPiece(self, field):
        # print(field.position)
        if field in self.WhitePiecesFields():
            # print("luam piesa alba")
            for whitepiece in self.whitePieces:

                if whitepiece.field == field:
                    return whitepiece
        elif field in self.BlackPiecesFields():
            # print("luam piesa neagra")
            for blackpiece in self.blackPieces:
                if blackpiece.field == field:
                    return blackpiece

        else:
            # print("nu avem piesa pe campul asta")
            return None

    def BlackPiecesFields(self):
        fields = []
        for blackpiece in self.blackPieces:
            fields += [blackpiece.field]

        return fields

    def WhitePiecesFields(self):
        fields = []
        for whitepiece in self.whitePieces:
            fields += [whitepiece.field]

        return fields

    def __str__(self):
        stringBoard = ""
        whitepiecespositions = []
        blackpiecespositions = []
        for i in range(0, 8):
            lineShown = ""
            for j in range(0, 8):
                for whitepiece in self.whitePieces:
                    if (7 - i, j) == whitepiece.field.position:
                        lineShown += " " + str(whitepiece) + " "
                        whitepiecespositions += [whitepiece.field.position]
                for blackpiece in self.blackPieces:
                    if (7 - i, j) == blackpiece.field.position:
                        lineShown += " " + str(blackpiece) + " "
                        blackpiecespositions += [blackpiece.field.position]

                if ((7 - i, j) not in whitepiecespositions) and ((7 - i, j) not in blackpiecespositions):
                    lineShown += " " + str(self.BoardFields[8 * i + j]) + " "
            stringBoard += lineShown + '\n'
        return stringBoard
