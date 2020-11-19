#In this program we will rename all File in a directory:-

import os
# Your_path=os.chdir(input("Enter your path here ="))               #Here we are taking the 'path from the user' where we have to rename the files.
Your_path=os.chdir("C:/Users/Anirudh/Downloads/test")            #This is path used for testing purpose
print("\nThis is the new working dir =",[ os.getcwd() ])      #Here we print the 'new given path'..

Tag1=input("Enter the 'char' or 'string' just before the required name =")
Tag2=input("Enter the 'char' or 'string' just after the required name =")
fextension=input("Enter the file extension here with a '.' =")
# File_list=os.listdir(Your_path)           #Here we are getting list of File-Folder

File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]    #Here we are getting list of File


#----------------------If You Want To Rename The Filelist To It's First Name----------------------#
if Tag1== "":
	for i in range(len(File_list)):           #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag2)[0]  
		d=f"{Split1}{fextension}"
		# print(d)
		os.rename(File_list[i],d)            #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To It's Last Name----------------------#
elif Tag2== "":
	for i in range(len(File_list)):         #Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)[1]   
		d=f"{Split1}"
		# print(d)
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


#----------------------If You Want to Rename The Filelist To a particular string/character/number----------------------#
else:
	for i in range(len(File_list)):			#Here we are iterrating the loop for number of time 'the no. of elements in list'.
		Split1 = File_list[i].split(Tag1)   #Here we split each string of the list(ie, 'File_list') by " given Tag1 "
		Split2 = Split1[1].split(Tag2)[0]   #Here we split each string of 'Split1[1]'(ie, second-part[1] of  the strings of Split1) by " given Tag2 " and store the first part of the string(ie. [0] in Split2)
		d=f"{Split2}{fextension}"
		# print(d)
		os.rename(File_list[i],d)          #Here we rename the file as "os.rename(initial_name,final_name)"


print("Congratulations!! The file-names are chaged!!")

New_File_list = [f.name for f in os.scandir(Your_path) if f.is_file()]      #Here we are getting new list of File

#----------------------Printing Initial and Finall filename list----------------------#
print("\nThis was the inital namelist of files =")
print(*File_list, sep="\n")
print("\nThis is the new namelist of files =")
print(*New_File_list, sep="\n")

print("A program made by Lucifer!!")
