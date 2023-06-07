from lib.Dia1 import calculate_distance

def test_calculate_distance():
	with open("input.txt") as file:
		input = file.read().strip()

	assert calculate_distance(input) == 5