"""Bubble sort"""

numbers = [8,6,4,2,7,5,1,9,3]
count = 1
countw = 1
while count != 0:
	count = 0
	for x in range (len(numbers) - countw):                                                           
		if numbers[x] > numbers[x+1]:
			count += 1
			n1 = numbers[x]
			n2 = numbers[x + 1]
			numbers[x] = n2
			numbers[x + 1] = n1
	countw += 1
print(numbers) 