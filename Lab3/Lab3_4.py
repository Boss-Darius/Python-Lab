'''Lab3 4'''

'''The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
Build and return a string that represents the corresponding XML element.'''
'''
 Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
 returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "


'''

def build_xml_element(tag,value,**ceva):

    progres='<'+str(tag)+' '

    for key in ceva:
        progres=progres+str(key)+" \" "+str(ceva[key])+' \\ \"'

    progres=progres+'> '+str(value)+''
    return progres



print(build_xml_element("a","Hello there",href =" http://python.org ", _class =" my-link ", id= " someid "))