# CREATED BY:			Carl Peahota
# CREATION DATE:		1/9/2017
# This is accepting 2 inputs:
#	strFilename:		User enters a path and the name of a TXT file

# ******************************************************************************************************************************************
# *****************************************************************************************************************************************
# MODIFIED BY:			Carl Peahota
# MODIFICATION DATE:	1/9/2017
# ISSUES:				
#	Major:				NONE
#	Minor:				NONE
# ******************************************************************************************************************************************
# ******************************************************************************************************************************************
import os

os.system('cls')

def count_char(textCaps, char):
	count = 0
	for c in textCaps:
		if c == char:
			count += 1
	return count

strFilename = "C:\Python\PythonProjects\TextFiles\Test2.txt"

print("Here is the frequency of characters used in the file: " + strFilename)
print("")
	
with open(strFilename) as f:
  text = f.read()
  textCaps = text.upper()	# Convert the entire text to capital letters

    
for char in " ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	cnt = count_char(textCaps, char)
	perc = 100 * count_char(textCaps, char) / len(textCaps)
	print("{0} - {1} - {2}%".format(char, cnt, round(perc, 2)))
  
  
