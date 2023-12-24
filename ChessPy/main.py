from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen

from Field import Field
from Field import ChessBoard

# pionnegru=Pawn.Pawn(Field.BoardField((6,2)),"black")

tabla = ChessBoard.Board([], [])

rege = King.King(tabla, (0, 4), "white")
pion = Pawn.Pawn(tabla, (1, 3), "white")
pion2 = Pawn.Pawn(tabla, (1, 1), "white")
cal = Knight.Knight(tabla, (4, 3), "white")
tura = Rook.Rook(tabla, (0, 7), "white")
tura2= Rook.Rook(tabla,(0,0),"white")
nebun = Bishop.Bishop(tabla, (4, 4), "white")
dama = Queen.Queen(tabla, (6, 6), "white")
pionnegru = Pawn.Pawn(tabla, (6, 2), "negru")

variabila = 1
variabila = "acum sunt un sir de caractere"

variabila = [1, "acum sunt un string", 1.01]

piesacurenta = rege
print(piesacurenta.AttackMoves())
while True:
    # piesa=None
    # for whitepiece in tabla.whitePieces:
    #    if whitepiece.field==piesacurenta.field:
    #       piesa=whitepiece
    #       break
    # if piesa.__class__ != piesacurenta.__class__: piesacurenta=piesa

    print(piesacurenta.PrintPosition())
    print()
    print(piesacurenta, " ", piesacurenta.PossibleMoves())
    print()
    print(tabla)
    print()
    print(tabla.OccupiedField())
    print()
    print("row=")
    row = int(input())
    print("col=")
    col = int(input())

    camp = tabla.BoardFields[(7 - row) * 8 + col]
    piesacurenta.Move(camp)
    print("acum m-am multat la ", piesacurenta.PrintPosition())
    print("pot merge in ", piesacurenta.PossibleMoves())
