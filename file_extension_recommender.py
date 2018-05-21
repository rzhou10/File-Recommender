import os
import json

inputFile = raw_input("Want to know what program is best for your file? Check here! ")

#get file extension
filename, filename_extension = os.path.splitext(inputFile)

with open('List_of_programs.json') as json_data:
    json_object = json.load(json_data)

if filename_extension in json_object:
    #avoids issues of keys with different values, will ask user for their OSs
    osUsed = raw_input("Which OS do you use? ")
    if osUsed == "Windows":
        print "Recommended programs for Windows: " + json_object[filename_extension]["Windows"]
    elif osUsed == "Mac":
        print "Recommended programs for Mac: " + json_object[filename_extension]["Mac"]
    elif osUsed == "Linux" or osUsed == "Ubuntu":
        print "Recommended programs for Linux: " + json_object[filename_extension]["Linux"]
    else:
        print "Don't seem to know that OS."
else:
    print "File type doesn't exist, is misspelled, or not listed"