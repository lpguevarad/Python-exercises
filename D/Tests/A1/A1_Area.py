import math

	
def area_triangulo(s1,s2,s3):
	s = (s1+s2+s3)*0.5 #perimetro
	area = ( s* (s-s1) * (s-s2) * (s-s3))**0.5
	return area
	
l1 = input('Ingresar valor de 1er lado: ')
l2 = input('Ingresar valor de 2do lado: ')
l3 = input('Ingresar valor de 3er lado: ')

lado1=int(l1)
lado2=int(l2)
lado3=int(l3)

#print(area_triangulo(lado1, lado2,lado3))
print('El area del triangulo con los lados dados, es: ',round(area_triangulo(lado1,lado2,lado3),1))
