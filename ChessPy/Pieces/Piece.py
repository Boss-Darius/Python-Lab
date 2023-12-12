from Field import  Field
class Piece:
    def __init__(self,position,color):
        self.field=Field.BoardField(position)
        self.field.occupied=True
        self.color=color

    def PrintPosition(self):
        return self.field.PrintPosition()

    def Move(self,newfield):
        if not newfield.occupied:
            self.field.ChangeStatus()
            self.field=newfield
            newfield.ChangeStatus()
        else:
            print("This field is occupied")