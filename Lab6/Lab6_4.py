'''

Write a Python script that counts the number of files with each extension in a given directory.
The script should:
-Accept a directory path as a command line argument (using sys.argv).
-Use the os module to list all files in the directory.
-Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
-Include error handling for scenarios such as the directory not being found,
no read permissions, or the directory being empty.
'''

import sys
import os

try:
    assert (len(sys.argv)==2), "invalid numbers of parameters"

    directory=sys.argv[1]

    if(os.path.isdir(directory)):
        print("director valid :)")

        for element in os.walk(directory):
            print(element)
            elementList=list(element)

        print(elementList)
        files=elementList[2]
        subdirs=elementList[1]

        print(files,'-',subdirs)

        if len(files)==0:
            print("director gol!")

        else:
            extensions=dict()

            for file in files:
                filename,fileextension=os.path.splitext(directory+'\\'+file)
                extensions[fileextension]=0

            for extension in extensions:
                for file in files:
                    if file.endswith(extension):
                        extensions[extension]+=1

            print(extensions)

    else:
        print("director invalid :(")

except Exception as opsie:
    print(opsie)