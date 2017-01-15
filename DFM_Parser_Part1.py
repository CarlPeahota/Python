# ISSUES:	



import os

def Blank_Entry(strFile):
	# Checking the File_List.txt file
	if strFileListPath == strFile:
		if strFile == "":
			print("The Path and File for the File_List was not populated")
			input("Press Enter to continue...")
	# Checking the Array_Object_Types.txt file
	if strObjTypePath == strFile:
		if strFile == "":
			print("The Path and File for the Array Object Type File_List was not populated")
			input("Press Enter to continue...")

def File_NotExist(strFile):
	# Check for the existance of the path and file
	from pathlib import Path
		# Checking the File_List.txt file
	if strFileListPath == strFile:
		strFile = Path(strFileListPath)
		if not strFile.is_file():
			print("The File_List file does not exist")
			input("Press Enter to continue...")
	# Checking the Array_Object_Types.txt file
	if strObjTypePath == strFile:
		strFile = Path(strObjTypePath)
		if not strFile.is_file():
			print("The Array Object Type file does not exist")
			input("Press Enter to continue...")


		


		
#while True:
os.system('cls')
#strFileListPath = input("What is the full path of the File_List text file? ")
print("Please be sure that the file named File_List.txt is in C:\Python\PythonProjects\DFM Files\Definitions directory...")
#strObjTypePath = input("...and what is the full path of the Array Object Type text file ?")
print("and be sure that the file named Array_Object_Types.txt is there, too.")
input("Press Enter to continue...")

strFileListPath = 'C:\Python\PythonProjects\DFM Files\Definitions\File_List.txt'
strObjTypePath =  'C:\Python\PythonProjects\DFM Files\Definitions\Array_Object_Types_List.txt'

#os.system('cls')
	
	#try:
		# Check to see if the variables were left blank
Blank_Entry(strFileListPath)
Blank_Entry(strObjTypePath)
File_NotExist(strFileListPath)
File_NotExist(strObjTypePath)
	#except:
	#	print("An Error Occured")
	#	raise		