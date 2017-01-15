# CREATED BY:			Carl Peahota
# CREATION DATE:		1/14/2017
# INPUT(S)  - (s)tatic, (d)ynamic
#	pathOutput:			(s) - This is the fixed path where all TXT output files will go.
#	listTypeLabel:		(s) - Part of the naming convention for the output file.
#	fileExt:			(s) - Part of the naming convention for the output file.
#	timestp:			(s) - Part of the naming convention for the output file.
#	strFileListPath		(s) - this is where the list of DFM file paths are located
#	strObjTypePath		(s) - this is where the list of object types (TCxnQuery, etc.) are located
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# MODIFIED BY:			[Your Name]
# MODIFICATION DATE:	m/d/yyyy
# ISSUES:				
#	Major:				NONE
#	Minor:				NONE
# MODIFICATIONS:		NONE
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************

import os, datetime

strFileListPath = 'C:\Python\PythonProjects\DFM Files\Definitions\File_List.txt'
strObjTypePath =  'C:\Python\PythonProjects\DFM Files\Definitions\Array_Object_Types.txt'
pathOutput = 'C:\Python\PythonProjects\DFM Files\Output'
listTypeLabel = '\Object_Property_Lisiting_'
fileExt = '.txt'		
timestp = datetime.datetime.now().strftime('_%Y%m%d_%I%M%p')

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

def DelFile_Funct():
	path = pathOutput
	for file in os.scandir(path):
		if file.name.endswith(".txt"):
			os.remove(file.path)

# Read in the dfm file and the object type
def Read_Funct(strFileAndPathIn,listType):
	os.system('cls')
	fileSource = open(strFileAndPathIn, "r")
	lines = fileSource.readlines()

	cnt = 0		# the record line number within the source file
	recs = 0	# the cumulative count of records coming back (printed)
	flag = 0	# false by default
	for line in lines:
		line = line.strip()
		cnt = cnt + 1
		
		# the flag is set to 1 when the line starts w/ 'object' and ends w/ listType. The line is printed.
		if line.startswith('object') and line.endswith(listType):
			fileOut = open("".join([pathOutput, listTypeLabel, listType, timestp, fileExt]), "a")
			fileOut.write("------------------------------------------------------------------------------------------------------" + '\n')
			fileOut.write(str(cnt) + ' - ' + line + '\n')
			recs = recs + 1
			flag = 1
	
		# the flag is set to 0 when the line starts w/ 'object' and DOES NOT end w/ 'TCxnQuery'
		elif line.startswith('object') and not line.endswith(listType):
			flag = 0
		
		# the flag is set to 0 when the line DOES NOT start w/ 'object' and the flag was already 0
		elif not line.startswith('object') and flag == 0:
			flag = 0			
		
		# the flag is set to 1 when the line DOES NOT start w/ 'object' and the flag was already 1. This means that the line
		# was part of the object that the user wishes to capture. The line is printed.
		elif not line.startswith('object') and flag == 1:
			fileOut.write(str(cnt) + ' - ' + line + '\n')
			recs = recs + 1	
			flag = 1
			
			
	## The total records aquired is printed AFTER all lines are iterated
	#print()
	#print("=====================================")
	#print("There are " + str(recs) + " records")
	#print("=====================================")
	
	#fileOut.close()
	fileSource.close()
		


		
#while True:
os.system('cls')
#strFileListPath = input("What is the full path of the File_List text file? ")
print("Please be sure that the file named File_List.txt is in C:\Python\PythonProjects\DFM Files\Definitions directory...")
#strObjTypePath = input("...and what is the full path of the Array Object Type text file ?")
print("and be sure that the file named Array_Object_Types.txt is there, too.")
input("Press Enter to continue...")

os.system('cls')

Blank_Entry(strFileListPath)
Blank_Entry(strObjTypePath)
File_NotExist(strFileListPath)
File_NotExist(strObjTypePath)
DelFile_Funct()	

fileSource_FileList = open(strFileListPath, "r")
line_FileList = fileSource_FileList.readlines()

fileSource_ObjList = open(strObjTypePath, "r")
line_ObjList = fileSource_ObjList.readlines()

for lines_FileList in line_FileList:
	lines_FileList = lines_FileList.strip()
	
	for lines_ObjList in line_ObjList:
		lines_ObjList = lines_ObjList.strip()
		print("...working...")
		
		Read_Funct(lines_FileList,lines_ObjList)
		
print("Process complete.")