#In this program we will rename all File in a directory:-

#Type1:-
import os
# New_dir=os.chdir(input("Enter your path here ="))                     #Here we are taking the 'path from the user' where we have to rename the files.
New_dir=os.chdir("C:/Users/Anirudh/Downloads/TEST FOLDER 1")            #This is path used for testing purpose
print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..

spt1=input("Enter the 'char' or 'string' just before the required name =")
spt2=input("Enter the 'char' or 'string' just after the required name =")
fextension=input("Enter the file extension here with a '.' =")
File_list=os.listdir(New_dir)           #Here we are getting list of File-Folder

for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
    Split1 = File_list[i].split(spt1)   #Here we split each string of the list(ie, 'File_list') by "_-_"
    Split2 = Split1[1].split(spt2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by "_" and store the first part of the string(ie. [0] in Split2)
    d=f"{Split2}{fextension}"
    # print(d)
    os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"

print("Congratulations!! The file-names are chaged!!")


# #Type 2:-
# import test1234
# import os
# # New_dir=os.chdir(input("Enter your path here ="))                     #Here we are taking the 'path from the user' where we have to rename the files.
# New_dir=os.chdir("C:/Users/Anirudh/Downloads/TEST FOLDER 1")            #This is path used for testing purpose
# print("\nThis is the new 'current working dir' =",[ os.getcwd() ])      #Here we print the 'new given path'..
#
# spt1=input("Enter the 'char' or 'string' just before the required name =")
# spt2=input("Enter the 'char' or 'string' just after the required name =")
# fextension=input("Enter the file extension here with a '.' =")
# File_list=os.listdir(New_dir)           #Here we are getting list of File-Folder
#
# mn=test1234.ff
# if mn==1:
#     for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
#         Split1 = File_list[i].split(spt1)   #Here we split each string of the list(ie, 'File_list') by "_-_"
#         Split2 = Split1[1].split(spt2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by "_" and store the first part of the string(ie. [0] in Split2)
#         d=f"{Split2}{fextension}"
#         # print(d)
#         os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"
#
#     print("Congratulations!! The file-names are chaged!!")
# else:
#     pass




