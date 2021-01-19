"""Minimum selection"""

numbers = [8,6,4,2,7,5,1,9,3]
count = 0
while count != len(numbers):
	m = numbers[count]
	var = numbers[count]
	for y in range(count,len(numbers)):
		if m > numbers[y]:
			m = numbers[y]
			pos = y
	numbers[count] = m
	numbers[pos] = var
	count += 1
print(numbers)