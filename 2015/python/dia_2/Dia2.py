with open('input.txt', 'r') as file:
	inputFile = file.read()

sumatoria = 0
box = inputFile.split("\n")

for i in box:
	part = i.split("x")
	for i in part:
		boxMap = {'l': part[0], 'w': part[1], "h": part[2]}
	area = (2* (int(boxMap['l']) * int(boxMap['w'])) ) + (2* (int(boxMap['w']) * int(boxMap['h'])) ) + (2* ( int(boxMap['h']) * int(boxMap['l']) ) )
	small = min(int(boxMap['l']) * int(boxMap['w']), int(boxMap['w']) * int(boxMap['h']), int(boxMap['h']) * int(boxMap['l']) )
	area += small
	sumatoria += area
print("sumatoria: ",sumatoria)











	
