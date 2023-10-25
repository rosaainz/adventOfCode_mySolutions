with open('input.txt', 'r') as file:
	inputFile = file.read()

	print(inputFile) 


	floor = 0
	position = 1

	for i in inputFile:
		if i == '(':
			floor += 1
			
		elif i == ')':
			floor -= 1
			

		if floor == -1 :
			print("enter the basement in position: ",position)
			break
		print("position: ",position)
		position += 1;


