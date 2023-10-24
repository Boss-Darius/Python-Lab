'''Lab2_9'''

'''Write a function that receives as paramer a matrix which represents the heights of the spectators 
in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator 
which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him.
 All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, 
 beginning with the closest row from the field.'''


def cantSee(Field):
    unfortunateViewers=[]

    for i in range(0,len(Field)):
        for j in range(1,len(Field[i])):
            print('Field[i][j]',Field[i][j])
            for k in range(0,j):
                print('Field[i][k]',Field[i][k])
                if Field[i][k]> Field[i][j]:
                    t=tuple([i,j])
                    if unfortunateViewers.count(t)==0:
                        unfortunateViewers+=[t]

    return unfortunateViewers

Field=[
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

print(cantSee(Field))

