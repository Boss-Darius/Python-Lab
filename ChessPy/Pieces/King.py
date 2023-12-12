from Field import Field
from Pieces import Piece
class King(Piece.Piece):
    def __init__(self,field,color):
        self.field = field
        self.field.occupied = True
        self.color = color
        self.moved=False
        self.canCastle=True

    def PossibleMoves(self):
        moves=[]
        row=self.field.position[0]
        col=self.field.position[1]
        #checking if the king can move down
        if(col!=0):
            # move down
            moves += [chr(65 + col - 1) + str(row+1)]
            # move down left
            if(row!=0):
                moves += [chr(65 + col - 1) + str(row)]
            # move down right
            if (row != 7):
                moves += [chr(65 + col - 1) + str(row+2)]
        #
        # checking if the king can move up
        if (col != 7):
            # move up
            moves += [chr(65 + col + 1) + str(row+1)]
            # move up left
            if (row != 0):
                moves += [chr(65 + col + 1) + str(row)]

            # move up right
            if (row != 7):
                moves += [chr(65 + col+1) + str(row+2)]

        #checking if the king can move to the right
        if (row!=7): moves+=[chr(65+col)+str(row+2)] #moving right
        #checking if the king can move to the left
        if(row!=0): moves += [chr(65+col)+str(row)] #moving left

        return moves

    def Move(self,newfield):
        if str(newfield) in self.PossibleMoves():
            if not newfield.occupied:
                self.field.ChangeStatus()
                self.field = newfield
                newfield.ChangeStatus()
        else:
            print("That is not a correct move for the king")
    def __str__(self):
        return 'K'

