nums = []

print("This will show all values in the 5-times table, up to a max number.")
i = int(input("Enter a max number: "))

j= i - 1

i = 0
while i <= j:
	nums.append(5*i)
	i = i + 1
	
print(nums)