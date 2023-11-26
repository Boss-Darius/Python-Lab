'''

Create a Python script that calculates the total size of all files in a directory provided
as a command line argument. The script should:

-Use the sys module to read the directory path from the command line.
-Utilize the os module to iterate through all the files in the given directory and
its subdirectories.
-Sum up the sizes of all files and display the total size in bytes.
-Implement exception handling for cases like the directory not existing,
permission errors, or other file access issues.


'''
import sys
import os

try:
    assert (len(sys.argv)==2),"invalid numbers of parameters"

    directory=sys.argv[1]

    if(os.path.isdir(directory)):
        print("director valid :)")
        size=0

        for (root, directories, files) in os.walk(directory):
            for fileName in files:
                try:
                    full_fileName = os.path.join(root, fileName)
                    size+=os.stat(full_fileName).st_size
                except:
                    print("Probleme la fisiere :(")

        print("dimensiunea directorului "+directory+' :')
        print(size," (Bytes)")
        print(size/(1024**2)," (MB)")

    else:
        print("director invalid :(")
except Exception as e:
    print(e)