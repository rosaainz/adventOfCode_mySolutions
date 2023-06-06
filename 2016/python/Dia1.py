


def calculate_distance(input):
	list_input = input.split(", ")
	
	acum = 0
	for i in list_input:
		print(i[0], i[1])
		acum += int(i[1])

		#if( i[0] == 'R'):
		#	acum += int(i[1])
		#elif( i[0] == 'L'):
		#	acum -= int(i[1])

		print(acum)
	return acum


input = "R2, L3"
input2 = "R2, R2, R2"

position = (0,0)

assert calculate_distance(input) == 5, "no coincide"
assert calculate_distance(input2) == 2, "no coincide"



