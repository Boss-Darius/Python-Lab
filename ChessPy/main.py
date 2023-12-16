from Pieces import King
from Pieces import Pawn
from Pieces import Bishop
from Pieces import Knight
from Pieces import Rook
from Pieces import Queen

from Field import Field
from Field import ChessBoard



#pionnegru=Pawn.Pawn(Field.BoardField((6,2)),"black")

tabla=ChessBoard.Board([],[])

rege=King.King(tabla,(0,4),"white")
pion=Pawn.Pawn(tabla,(1,3),"white")
pion2=Pawn.Pawn(tabla,(1,1),"white")
cal=Knight.Knight(tabla,(4,3),"white")
tura=Rook.Rook(tabla,(5,5),"white")
nebun=Bishop.Bishop(tabla,(4,4),"white")
dama=Queen.Queen(tabla,(6,6),"white")

while True:
   print(nebun.PrintPosition())
   print()
   print("dama: ",dama.PossibleMoves())
   print()
   print(tabla)
   print()
   print(tabla.OccupiedField())
   print()
   print("row=")
   row = int(input())
   print("col=")
   col = int(input())

   camp = tabla.BoardFields[(7-row)*8+col]
   dama.Move(camp)

   print("dama.printprosition(): ",dama.PrintPosition())
   print("dama.possiblemoves(): ",dama.PossibleMoves())
