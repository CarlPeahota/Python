# ISSUES: When choosing "w" but a bogus path, I still get asked the question about what I want to write
# This is accepting 2 inputs:
#	strFileAction:	user enters (R)ead, (W)rite, or (A)ppend
#	strPath:		user enters a path and the name of a TXT file



while True:

	strFileAction = input("Would you like to (R)ead, (W)rite, or (A)ppend to a file?")
	strFileAndPath = input("What is the path AND file name that you wish to use?")

	if (strFileAndPath == "") or (strFileAction == ""):
		print("Missing Value!")
		continue
	else:
		print("")
		print("---------------")
		print("So far so good!")
		print("---------------")
		print("")
  
		if strFileAction.upper() == "R":
			print("R was chosen") 
			try:
				file = open(strFileAndPath, "r")
				cont = file.read()
				print(cont)
				file.close()
			except FileNotFoundError:
				print("Sorry, pal, but that path or file does not exist!")
			finally:
				break			
		elif strFileAction.upper() == "W":
			print("W was chosen")
			try:
				file = open(strFileAndPath, "w")
				str = input("What do you want to WRITE (NOTE: exisiting contents will be overwritten)?")
				file.write(str)
				file.close()
			except FileNotFoundError:
				print("Sorry, pal, but that path or file does not exist!")
			finally:
				break		
		elif strFileAction.upper() == "A":
			print("A was chosen")	
			file = open(strFileAndPath, "a")
			str = input("What do you want to APPEND?")
			file.write(str)
			file.close()			
			break
   