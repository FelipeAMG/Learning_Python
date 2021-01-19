import json,csv

with open('users_database.json', 'r') as json_file:
	pythonic_json = json.load(json_file)

csv_json = {}
with open('users_database.csv', mode='r') as csv_file:
	reader = csv.DictReader(csv_file)
	for rows in reader:
		id = rows['id']
		csv_json[id] = rows

with open('cvs_to_json', 'w') as json_file_csv:
	json.dump(csv_json, json_file_csv)

for x in range(len(pythonic_json)):
	for y in range(len(pythonic_json)):
		if pythonic_json[y]['id'] == x + 1:
			print(type(pythonic_json[y]['id']))
			print(pythonic_json[y])
			z = str(x + 1)
			print(csv_json[z])

