from Pieces import Piece

class Bishop(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table=table
        self.field = self.table.BoardFields[(7-position[0])*8+position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PossibleMoves(self):
        possiblemoves=[]

        col=self.field.position[1]
        row=self.field.position[0]
        chessboard= self.table.BoardFields

        #cheking if the bishop can move down

        if row!=0:
            r1=row
            c1=col
            #down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8*(7-r1)+c1].occupied==False:
                    print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1+1)]
                    c1 -= 1
                    r1 -= 1
                elif r1==row and c1==col:
                    print("camp original")
                    c1 -= 1
                    r1 -= 1
                    continue

                else: break

            r1 = row
            c1 = col
            # down right
            while r1 >= 0 and c1 <=7:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 += 1
                    r1 -= 1
                elif r1 == row and c1 == col:
                    print("camp original")
                    c1 += 1
                    r1 -= 1
                    continue

                else:
                    break
        #checking if the bishop can move up
            if row != 7:
                r1 = row
                c1 = col
                # up left
                while r1 <=7 and c1 >= 0:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                        print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 -= 1
                        r1 += 1
                    elif r1 == row and c1 == col:
                        print("camp original")
                        c1 -= 1
                        r1 += 1
                        continue

                    else:
                        break

                r1 = row
                c1 = col
                # up right
                while r1 <= 7 and c1 <= 7:
                    if chessboard[8 * (7 - r1) + c1].occupied == False:
                        print("camp bun")
                        possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                        c1 += 1
                        r1 += 1
                    elif r1 == row and c1 == col:
                        print("camp original")
                        c1 += 1
                        r1 += 1
                        continue

                    else:
                        break
            return possiblemoves

    def Move(self, newfield):
        if str(newfield) in self.PossibleMoves():
            if not newfield.occupied:
                self.field.ChangeStatus()
                self.field = newfield
                newfield.ChangeStatus()
        else:
            print("That is not a correct move for the bishop")

    def __str__(self):
        return "N "
