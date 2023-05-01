with open('input.txt', 'r') as file:
	inputFile = file.read()

	print("leyendo file")
	print(inputFile) 


	floor = 0
	position = 1

	print("floor inicial: ",floor)
	for i in inputFile:
		if i == '(':
			floor += 1
			print("floor en if (: ",floor)
		elif i == ')':
			floor -= 1
			print("floor en if ): ",floor)
	print(floor)		