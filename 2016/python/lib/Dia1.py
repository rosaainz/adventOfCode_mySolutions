


def calculate_distance(path):
	with open(path) as file:
		input = file.read().strip()

	list_input = input.split(", ")
	
	acum = 0
	for i in list_input:
		print(i[0], i[1])
		acum += int(i[1])

		print(acum)
	return acum




