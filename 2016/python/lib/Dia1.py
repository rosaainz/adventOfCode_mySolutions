

def calculate_distance(path_file):
	with open(path_file) as file:
		input = file.read().strip()

	list_input = input.split(", ")

	coordinates = [
			{'L': -1, 'R':1}, #N
			{'L': -1, 'R':1}, #E
			{'L': 1, 'R':-1}, #S
			{'L': 1, 'R':-1}  #W
	]


	
	acum = 0
	for i in list_input:
		print(i[0], i[1])
		acum += int(i[1])

		print(acum)
	return acum




