from lib.Dia1 import calculate_distance

def test_calculate_distance():
	input = "R2, L3"
	input2 = "R2, R2, R2"

	assert calculate_distance(input) == 5, "no coincide"