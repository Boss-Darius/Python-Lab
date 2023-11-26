'''

Write a script using the os module that renames all files in a specified directory to have
a sequential number prefix. For example, file1.txt, file2.txt, etc.
Include error handling for cases like the directory not existing or files that can't be renamed.

'''
import os
import os.path as cale

print("Director:")
directory=input()



if(cale.isdir(directory)):
    print("Director valid")
    print("Prefix:")
    prefix = input()
    index=1
    for (root,directories,files) in os.walk(directory):
        for file in files:
            try:
                os.renames(directory+'\\'+file,directory+'\\'+prefix+str(index))
                index+=1
            except:
                print("Unable to rename file")

    for (root,directories,files) in os.walk(directory):
        for file in files:
            print(file)


else :
    print("Director invalid")