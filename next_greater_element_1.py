## http://www.geeksforgeeks.org/next-greater-element/
numbers=[24,2,4]
length=len(numbers)

i=0
while(i<length-1):
	j=i+1
	flag=False
	while(j<length):
		if numbers[j]<numbers[i]:
			j=j+1
		else:
			for k in range(i,j):
				print numbers[j]
			flag=True
			i=j
			break
	if not flag:
		print -1
		i=i+1
print -1