#
# gire a la izquierda (L) o a la derecha (R) 90 grados
#


input = "R2, L3"

def calculate_distance(input):
	list_input = input.split(", ")
	
	for i in list_input:
		print(i)
	return 4
	

assert calculate_distance(input) == 5, "no coincide"



