lorem_ipsum = open("loremipsum.txt","r")
lorem_ipsum = lorem_ipsum.read()
count = 0
caps = 0
while count < len(lorem_ipsum):
	letter = lorem_ipsum[count]
	if letter.isupper() == True:
		caps +=1
	count += 1

print("Total caps: " , caps)