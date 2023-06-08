

def calculate_distance(path_file):
	with open(path_file) as file:
		input = file.read().strip()

	list_input = input.split(", ")

	quadrant = [
			{'L': -1, 'R':1}, #N 0
			{'L': -1, 'R':1}, #E 1 
			{'L': 1, 'R':-1}, #S 2 
			{'L': 1, 'R':-1}  #W 3
	]

	rotation = {'R':1, 'L':-1}

	direction = 0 #norte
	x,y = 0,0
	
	for i in list_input:
		turn = i[0]
		distance = int(i[1])

		sign = quadrant[direction][turn]   #+
		
		if direction%2==0:
			x += sign * distance
		else:
			y += sign * distance

		direction = (direction + 4 + rotation[turn]) % 4

	distance_final = abs(x) + abs(y)

	return distance_final




