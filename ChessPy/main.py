from Pieces import King
from Field import Field
from Field import ChessBoard
rege=King.King(Field.BoardField((0,4)),"white")


tabla=ChessBoard.Board([rege],[])


while True:
    print(rege.PrintPosition())
    print(rege.PossibleMoves())
    print(tabla)
    print("row=")
    row=int(input())
    print("col=")
    col=int(input())

    camp=Field.BoardField((row,col))
    rege.Move(camp)
