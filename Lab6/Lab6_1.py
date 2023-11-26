'''

Create a Python script that does the following:
-Takes a directory path and a file extension as command line arguments (use sys.argv).
-Searches for all files with the given extension in the specified directory (use os module).
-For each file found, read its contents and print them.
-Implement exception handling for invalid directory paths,
incorrect file extensions, and file access errors.


'''


import os
import sys

try:
    length=len(sys.argv[1:])
    assert (length >= 2), "Too few arguments " + str(length);
    assert (length <= 2), "Too many arguments" + str(length)


except Exception as opsie:
    print(opsie)
else:
    print("Arguments are ok")
    directory=sys.argv[1]
    extension="."+sys.argv[2]

    print(directory,'---',extension)

    if os.path.exists(directory) and os.path.isdir(directory):
        print("the directory is Valid")

        for (roots,directories,files) in os.walk(directory):
            for filename in files:
                if os.path.isfile(directory+'\\'+filename) and filename.endswith(extension):
                    print(filename)
                    print()
                    try:
                        content=open(directory+'\\'+filename,'rt').read();
                        print(content)
                        print()
                    except:
                        print("unable to open file")
    else: print("invalid directory")