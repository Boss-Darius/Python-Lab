from Pieces import Piece

class Queen(Piece.Piece):
    def __init__(self, table, position, color):
        self.color = color
        self.table=table
        self.field = self.table.BoardFields[(7-position[0])*8+position[1]]
        self.table.AddPiece(self)
        self.field.occupied = True

    def PossibleMoves(self):
        #adding the rook-like behavior
        possiblemoves = []

        col = self.field.position[1]
        row = self.field.position[0]
        chessboard = self.table.BoardFields
        # adding the horrizontal possible moves
        # adding the horrizontal possible moves
        # right
        for i in range(col + 1, 8):
            print(chr(65 + i) + str(row + 1))
            if chessboard[8 * (7 - (row)) + i].occupied == False:
                print("camp liber")
                possiblemoves += [chr(65 + i) + str(row + 1)]
            elif chessboard[8 * (7 - (row)) + i].occupied == True:
                print("camp ocupat")
                break
        print("left")
        # left
        for i in range(0, col):
            print(chr(65 + i) + str(row + 1))
            if chessboard[8 * (7 - (row)) + i].occupied == False:
                print("camp liber")
                possiblemoves += [chr(65 + i) + str(row + 1)]
            elif chessboard[8 * (7 - (row)) + i].occupied == True:
                print("camp ocupat")
                break

        # adding the vertical behavior
        # up
        for i in range(row + 1, 8):
            print(chr(65 + col) + str(i + 1))

            if chessboard[8 * (7 - i) + col].occupied == False:
                print("da")
                possiblemoves += [chr(65 + col) + str(i + 1)]
            else:
                print("nu")
                break
        # down
        for i in range(0, row):
            print(chr(65 + col) + str(i + 1))
            if chessboard[8 * (7 - i) + col].occupied == False:
                print("da")
                possiblemoves += [chr(65 + col) + str(i + 1)]
            else:
                print("nu")
                break

        # adding the bishop-like behavior
        if row != 0:
            r1 = row
            c1 = col
            # down left
            while r1 >= 0 and c1 >= 0:
                if chessboard[8 * (7 - r1) + c1].occupied == False:
                    print("camp bun")
                    possiblemoves += [chr(65 + c1) + str(r1 + 1)]
                    c1 -= 1
                    r1 -= 1
                elif r1 == row and c1 == col:
                    print("camp original")
                    c1 -= 1
                    r1 -= 1
                    continue

                else:
                    break

            r1 = row
            c1 = col
            # down right
            while r1 >= 0 and c1 <= 7:
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
            # checking if the bishop can move up
            if row != 7:
                r1 = row
                c1 = col
                # up left
                while r1 <= 7 and c1 >= 0:
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

    def Move(self,newfield):
        if str(newfield) in self.PossibleMoves():
            if not newfield.occupied:
                self.field.ChangeStatus()
                self.field = newfield
                newfield.ChangeStatus()
        else:
            print("That is not a correct move for the queen")


    def __str__(self):
        return "Q "