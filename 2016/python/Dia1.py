#
# gire a la izquierda (L) o a la derecha (R) 90 grados
#


input = "R2, L3"

def calculate_distance(input):
	list_input = input.split(", ")
	
	acum = 0

	for i in list_input:
		print(i[0], i[1])
		acum += int(i[1])
	return acum
	

assert calculate_distance(input) == 5, "no coincide"



