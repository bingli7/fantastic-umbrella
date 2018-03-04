import json



def json_dump_load():
	filename = "project.json"

	data = {
		'name'	: 'bingli',
		'age'	: '22'
	}
	# dumps from python type to json string
	json_string = json.dumps(data)
	print type(json_string)
	print json_string

	# loads to a python dict
	json_load = json.loads(json_string)
	print type(json_load)
	print json_load
	print 'my age: ', json_load['age']

	# load from a file to a python dict
	with open(filename, 'r') as file:
		file_data = json.load(file)
	print type(file_data)
	print file_data

	# dump
	new_filename = 'project_copy.json'
	with open(new_filename, 'w') as file:
		json.dump(file_data, file)

if __name__ == '__main__':
	json_dump_load()
