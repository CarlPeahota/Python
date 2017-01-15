# CREATED BY:			Carl Peahota
# CREATION DATE:		1/10/2017
# This is accepting ? inputs:
#	objType:			Currently called 'TCxnQuery'
#	FilePath_Output		Currently called 'C:\Python\PythonProjects\DFM Files\Output\'
#	FilePath_Input		Currently called 'C:\Python\PythonProjects\DFM Files\APPTTYPE.dfm'
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
# MODIFIED BY:			Carl Peahota
# MODIFICATION DATE:	1/11/2017
# ISSUES:				
#	Major:				NONE
#	Minor:				NONE
# MODIFICATIONS:		(1) added DelFile() function to delete all TXT files previously created by the program
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************

########################################################################################################################
########################################################################################################################
# be sure to add code to look for existance of file in both Read_Funct and DelFile_Funct. If file DNE, just skip it
########################################################################################################################
########################################################################################################################

import os, datetime

# This is the fixed path where all TXT output files will go.
pathOutput = 'C:\Python\PythonProjects\DFM Files\Output'

# These are fixed strings to be used as part of the name of the output file.
listTypeLabel = '\Object_Property_Lisiting_'
#listType = 'TCxnQuery'
fileExt = '.txt'		
timestp = datetime.datetime.now().strftime('_%Y%m%d_%I%M%p')

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
			print("------------------------------------------------------------------------------------------------------")
			print("".join([pathOutput, listTypeLabel, listType, timestp, fileExt]))
			print("------------------------------------------------------------------------------------------------------")
			fileOut.write("------------------------------------------------------------------------------------------------------" + '\n')
			print(str(cnt) + ' - ' + line)
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
			print(str(cnt) + ' - ' + line)
			fileOut.write(str(cnt) + ' - ' + line + '\n')
			recs = recs + 1	
			flag = 1
			
			
	# The total records aquired is printed AFTER all lines are iterated
	print()
	print("=====================================")
	print("There are " + str(recs) + " records")
	print("=====================================")
	
	fileOut.close()
	fileSource.close()

DelFile_Funct()	

#The files below work well, individually

#Read_Funct('C:\Python\PythonProjects\DFM Files\APPTTYPE.dfm','TCxnQuery')
#Read_Funct('C:\Python\PythonProjects\DFM Files\AuditTInput.dfm','TCxnQuery')
#Read_Funct('C:\Python\PythonProjects\DFM Files\BankAcct.dfm','TCxnQuery')
	
