from Pieces import Piece
class Rook(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table = table
        self.field = self.table.BoardFields[(7 - position[0]) * 8 + position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True
        self.moved = False
        self.canCastle = True
    def PossibleMoves(self):
        possiblemoves=[]

        col=self.field.position[1]
        row=self.field.position[0]
        chessboard=self.table.BoardFields

        #adding the horrizontal possible moves
        #right
        for i in range(col+1,8):
            print(chr(65+i)+str(row+1))
            if chessboard[8*(7-(row))+i].occupied==False:
                print("camp liber")
                possiblemoves+=[chr(65+i)+str(row+1)]
            elif chessboard[8*(7-(row))+i].occupied==True:
                print("camp ocupat")
                break
        print("left")
        #left
        for i in range(0, col):
            print(chr(65 + i) + str(row + 1))
            if chessboard[8 * (7 - (row)) + i].occupied == False:
                print("camp liber")
                possiblemoves += [chr(65 + i) + str(row + 1)]
            elif chessboard[8 * (7 - (row)) + i].occupied == True:
                print("camp ocupat")
                break

        #adding the vertical behavior
        #up
        for i in range(row+1,8):
            print(chr(65+col)+str(i+1))

            if chessboard[8*(7-i)+col].occupied==False:
                print("da")
                possiblemoves+=[chr(65+col)+str(i+1)]
            else:
                print("nu")
                break
        #down
        for i in range(0,row):
            print(chr(65+col)+str(i+1))
            if chessboard[8*(7-i)+col].occupied==False:
                print("da")
                possiblemoves+=[chr(65+col)+str(i+1)]
            else:
                print("nu")
                break

        return possiblemoves
    def Move(self,newfield):
        if str(newfield) in self.PossibleMoves():

            self.field.ChangeStatus()
            self.field = newfield
            newfield.ChangeStatus()
            self.moved = True
            self.canCastle = False
        else:
            print("That is not a correct move for the rook")

    def __str__(self):
        return "R "