

def calculate_distance(path_file):
	with open(path_file) as file:
		input = file.read().strip()

	list_input = input.split(", ")

	quadrant = [
			{'L': -1, 'R':1}, #N
			{'L': -1, 'R':1}, #E
			{'L': 1, 'R':-1}, #S
			{'L': 1, 'R':-1}  #W
	]

	rotation = {'R':1, 'L':-1}

	direction = 0
	x,y = 0,0
	
	return distance_final




