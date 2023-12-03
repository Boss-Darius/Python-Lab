import os

def FileConcatenation(fileList,order,separator):
    content=""

    try:
        for i in order:
            content+=open(fileList[i]).read()+separator
        open(fileList[order[0]]).write(content)

        for i in range(1,len(order)):
            os.remove(fileList[order[i]])
    except Exception as e:
            print(e)