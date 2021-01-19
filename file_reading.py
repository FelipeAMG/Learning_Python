"""File handling"""

# my_file = open('data.txt','r')

"""
with open('data.txt','r') as data:
	print(f'File name: {data.name}')
	print('Read:')
	print(data.read())
"""

"""
lines = ["This is line 5", "This is line 6", "This is line 7"]
with open('data.txt','a+') as data:
	for line in lines:
		data.write(line)
		data.write('\n')
"""

"""
lines = ["This is line 5", "This is line 6", "This is line 7"]
with open('data.txt','r') as data:
	data_as_list = data.readlines()

data_as_list.insert(1,"This is between line 1 and 2\n")

with open('data.txt','w') as data:
	data_as_str = "".join(data_as_list)
	data.write(data_as_str)

with open('data.txt','a+') as data:
	for line in lines:
		data.write(line)
		data.write('\n')
"""
#For binary data
lines = [b"This is line 5", b"This is line 6", b"This is line 7"]
with open('data.txt','rb') as data:
	data_as_list = data.readlines()

data_as_list.insert(1, b"This is between line 1 and 2\n")

with open('data.txt','wb') as data:
	for data_line in data_as_list:
		data.write(data_line)
	for line in lines:
		data.write(line)
		data.write(b'\n')

"""
Text files's modes:

w - write
r - read
a - append
r+ - read & write
x - creation mode

Text file's modes:

wb - write
rb - read
ab - append
rb+ - read & write
"""