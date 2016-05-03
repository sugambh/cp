## http://www.geeksforgeeks.org/next-greater-element/
numbers=[0,1]
for i in range(0,len(numbers)):
	flag=False
	if (i!=len(numbers)-1):
		for j in range(i+1,len(numbers)):
			if numbers[j]>numbers[i]:
				flag=True
				break
			j=j+1
		if j>=len(numbers):
			print -1
		else:
			print numbers[j]
	else:
		print -1
	i=i+1