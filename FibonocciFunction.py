# THIS IS WORKING
# INPUT: This is accepting 1 input
#	n:	user enters a max value for the Fibonocci sequence
# OUTPUT: a string of numbers, separated by commas, and sent to the console

n = int(input("Enter a max value for the Fibonocci sequence: "))

def ComputeFib(n):
	a, b = 0, 1
	while b < n:
		print(b, end=',')
		a, b = b, a+b

ComputeFib(n)