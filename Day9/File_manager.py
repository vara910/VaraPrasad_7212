import sys
file = open("sample.txt","w")
file.write("this is the first line iam writing in the file")
file.close()
# with open("sample.txt","w") as file:     #this thing overwrites the existing file
#     file.write("this is the second line")