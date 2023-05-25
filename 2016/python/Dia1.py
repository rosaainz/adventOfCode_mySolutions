#
#gire a la izquierda ( L) o a la derecha ( R) 90 grados
#
#Seguir R2, L3le deja 2cuadras al este y 3cuadras al norte, o 5cuadras de distancia.  ----- 
#    R2 SUMA 2
#    L3 SUMA 5

#R2, R2, R2lo deja 2a cuadras al sur de su posición inicial, que está 2a cuadras de distancia.
#	 R2 SUMA 2
#

#R5, L5, R5, R3te 12deja a cuadras.



#
# 1. leer la entrada que viene de la sig manera: R1, R2, L3 (letra valor a sumar o restar)
# 	1.1 separar por "," 
# 	1.2 obtener el primer caracter 
# 2. Dependiendo de si es L o R y del valor anterior, sumar o restar, si ya hay un R y el sig es otro R se va a restar. igual con la L
# 	2.1 guardar el primer ese caracter en una variable 
#	2.2 si el que viene es igual al anterior, restar 
#	2.3 si es diferente sumar 

entrada = input().split(",")

print(entrada)

