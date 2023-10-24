'''Lab2_4'''

'''4. Write a function that receives as a parameters a list of musical notes (strings),
 a list of moves (integers) and a start position (integer). The function will return the song composed by 
going though the musical notes beginning with the start position and following the moves given as parameter.'''

'''Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] '''


def compose(notesList, intList, position):
    song = []

    limit = len(notesList)
    song += [notesList[position]]

    for i in intList:
        position = position + i
        if position > limit:
            position = position % limit
        song += [notesList[position]]

    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))