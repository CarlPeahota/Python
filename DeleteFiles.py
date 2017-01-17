import os

print("gonna delete the file")
path = 'C:\Python\PythonProjects\DFM Files\Output'

for file in os.scandir(path):
	if file.name.endswith(".txt"):
		os.remove(file.path)

