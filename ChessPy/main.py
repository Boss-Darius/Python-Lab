import Pieces
from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen
import tkinter as tk
from PIL import ImageTk, Image

from Field import ChessBoard
from Players import Player
from Players import AI

from GUI import GUI
test=GUI.GUI()

tabla=ChessBoard.Board()
print(tabla)


Albul = Player.Player(tabla, "white")
Negrul = AI.AI(tabla,"black")

Albul.GetPieces()
Negrul.GetPieces()

print(Albul.pieces)
print(Negrul.pieces)

black=[str(piece) for piece in Negrul.pieces]; white=[str(piece) for piece in Albul.pieces]

print(black)
print(white)
# print(tura2.ShowFilteredInputMoves())
while True:
    print(tabla)
    if Albul.CheckMated():
        print(Albul.name + " a pierdut. " + Negrul.name + " a castigat")
        break

    Albul.GetPieces()
    white = [str(piece) for piece in Albul.pieces]
    print(white)
    Albul.InputMove()

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
    Negrul.InputMove()

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
    # print(piesacurenta, " pot merge in", piesacurenta.ShowFilteredInputMoves())
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
    # piesacurenta.InputMove(camp,piesacurenta.FilterInputMoves())
    #
    # for piece in tabla.blackPieces:
    #     if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
    #         piece.Enpassant=False
    #         break
    #
    # piesacurenta=ChooseBlackPiece(tabla)
    # print("acum m-am multat la ", piesacurenta.PrintPosition())
    # print("pot merge in ", piesacurenta.ShowFilteredInputMoves())
    # print("pot ataca la ", piesacurenta.AttackInputMoves())
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
    # piesacurenta.InputMove(camp,piesacurenta.FilterInputMoves())
    #
    # print(tabla)
    # for piece in tabla.whitePieces:
    #     if isinstance(piece,Pieces.Pawn.Pawn) and piece.Enpassant:
    #         piece.Enpassant=False
    #         break
    #
    # print("acum m-am multat la ", piesacurenta.PrintPosition())
    # print("pot merge in ", piesacurenta.FilterInputMoves())
    # print("pot ataca la ", piesacurenta.AttackInputMoves())
    # print(rege," in sah??? ", rege.InCheck())
    # print(regenegru," in sah??? ", regenegru.InCheck())

print(tabla)
