with open('input.txt', 'r') as file:
	inputFile = file.read()

total = 0
perimeter = 0
volume = 0
ribbon = 0
total_ribbon = 0
box = inputFile.split("\n")

for i in box:
	part = i.split("x")
	for i in part:
		boxMap = {'l': part[0], 'w': part[1], "h": part[2]}
	area = (2* (int(boxMap['l']) * int(boxMap['w'])) ) + (2* (int(boxMap['w']) * int(boxMap['h'])) ) + (2* ( int(boxMap['h']) * int(boxMap['l']) ) )
	small = min(int(boxMap['l']) * int(boxMap['w']), int(boxMap['w']) * int(boxMap['h']), int(boxMap['h']) * int(boxMap['l']) )
	area += small

##part 2
## 1. sacar perimetro: (ejemp: 2x3x4) Perímetro = 2largo + 2ancho =  2*2 + 2*3 = 4 + 6 = 10 pies
## 2. sacar volumen: Volumen = largo x ancho x alto = 2 x 3 x 4 = 24 pies cúbicos
## 3. sumarlos volumen + perimetro

	dimensions = list(part)
	perimeter = 2*int(dimensions[0]) + 2*int(dimensions[1])
	volume = int(boxMap['l']) * int(boxMap['w']) * int(boxMap['h'])
	ribbon = perimeter + volume
	total_ribbon += ribbon
	total += area
	
print("Total: ",total)
print("total ribbon: ",total_ribbon)