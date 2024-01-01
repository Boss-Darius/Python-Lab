import Pieces
from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen

from Field import ChessBoard
from Players import Player
from Players import AI


def ChooseWhitePiece(table):
    piese = table.whitePieces
    print("alegea piesa :")
    indice = int(input())

    if indice < 0:
        indice = 0
    elif indice > len(piese):
        indice = len(piese)

    return piese[indice]


def ChooseBlackPiece(table):
    piese = table.blackPieces
    print("alegea piesa :")
    indice = int(input())

    if indice < 0:
        indice = 0
    elif indice > len(piese):
        indice = len(piese)

    return piese[indice]


# tabla = ChessBoard.Board([], [])
#
# rege = King.King(tabla, (0, 4), "white")
# pion = Pawn.Pawn(tabla, (1, 3), "white")
# pion2 = Pawn.Pawn(tabla, (1, 1), "white")
# cal = Knight.Knight(tabla, (4, 3), "white")
# tura = Rook.Rook(tabla, (0, 7), "white")
# tura2 = Rook.Rook(tabla, (0, 0), "white")
# nebun = Bishop.Bishop(tabla, (4, 4), "white")
# dama = Queen.Queen(tabla, (6, 6), "white")
# pionnegru = Pawn.Pawn(tabla, (6, 2), "black")
# regenegru = King.King(tabla, (7, 4), "black")
# turaneagra = Rook.Rook(tabla, (7, 7), "black")
# turaneagra2 = Rook.Rook(tabla, (7, 0), "black")

# print(rege.ShowFilteredMoves())
# print(tura.ShowFilteredMoves())
tabla=ChessBoard.Board()
print(tabla)

# for piece in tabla.whitePieces:
#     print(piece," ",piece.PossibleMoves())
#
# for piece in tabla.blackPieces:
#     print(piece," ",piece.PossibleMoves())


Albul = Player.Player(tabla, "white")
Negrul = AI.AI(tabla,"black")

Albul.GetPieces()
Negrul.GetPieces()

print(Albul.pieces)
print(Negrul.pieces)

black=[str(piece) for piece in Negrul.pieces]; white=[str(piece) for piece in Albul.pieces]

print(black)
print(white)
# print(tura2.ShowFilteredMoves())
while True:
    print(tabla)
    if Albul.CheckMated():
        print(Albul.name + " a pierdut. " + Negrul.name + " a castigat")
        break

    Albul.GetPieces()
    white = [str(piece) for piece in Albul.pieces]
    print(white)
    Albul.Move()

    for piece in tabla.blackPieces:
        if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
            piece.Enpassant=False
            break
    if Negrul.CheckMated():
        print(Negrul.name + " a pierdut. " + Albul.name + " a castigat")
        break
    print(tabla)
    Negrul.GetPieces()
    black = [str(piece) for piece in Negrul.pieces]
    print(black)
    Negrul.Move()

    for piece in tabla.whitePieces:
        if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
            piece.Enpassant=False
            break

    # piesa=None
    # for whitepiece in tabla.whitePieces:
    #    if whitepiece.field==piesacurenta.field:
    #       piesa=whitepiece
    #       break
    # if piesa.__class__ != piesacurenta.__class__: piesacurenta=piesa
    # piesacurenta=ChooseWhitePiece(tabla)
    # print(piesacurenta.PrintPosition())
    # print()
    # print(piesacurenta, " pot merge in", piesacurenta.ShowFilteredMoves())
    # print()
    # print(tabla)
    # print()
    # print(tabla.OccupiedField())
    # print()
    # print("row=")
    # row = int(input())
    # print("col=")
    # col = int(input())
    #
    # camp = tabla.BoardFields[(7 - row) * 8 + col]
    # piesacurenta.Move(camp,piesacurenta.FilterMoves())
    #
    # for piece in tabla.blackPieces:
    #     if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
    #         piece.Enpassant=False
    #         break
    #
    # piesacurenta=ChooseBlackPiece(tabla)
    # print("acum m-am multat la ", piesacurenta.PrintPosition())
    # print("pot merge in ", piesacurenta.ShowFilteredMoves())
    # print("pot ataca la ", piesacurenta.AttackMoves())
    # print(rege," in sah??? ", rege.InCheck())
    # print(regenegru," in sah??? ", regenegru.InCheck())
    # print(tabla)
    # print()
    # print(tabla.OccupiedField())
    # print()
    # print("row=")
    # row = int(input())
    # print("col=")
    # col = int(input())
    #
    # camp = tabla.BoardFields[(7 - row) * 8 + col]
    # piesacurenta.Move(camp,piesacurenta.FilterMoves())
    #
    # print(tabla)
    # for piece in tabla.whitePieces:
    #     if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
    #         piece.Enpassant=False
    #         break
    #
    # print("acum m-am multat la ", piesacurenta.PrintPosition())
    # print("pot merge in ", piesacurenta.FilterMoves())
    # print("pot ataca la ", piesacurenta.AttackMoves())
    # print(rege," in sah??? ", rege.InCheck())
    # print(regenegru," in sah??? ", regenegru.InCheck())

print(tabla)
