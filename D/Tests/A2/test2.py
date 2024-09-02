
##################primera actividad. Modularidad de un numero

'''
def rango_numero (x:int)->int:
	if x<0:
		return -1
	elif x<1000:
		return 0
	elif x<=10000:
		return 1
	else:
		return 2

#Segunda version cambiando tener varios return


def rango_numero (x:int)->int:
	if x<0:
		respuesta = -1
	elif x<1000:
		respuesta = 0
	elif x<=10000:
		respuesta = 1
	else:
		respuesta = 2
		
	return respuesta

x=(int(input('ingrese numero: ')))
print(rango_numero(x))
'''

###################segunda actividad. Puntos colineales
'''
def son_colineales(x1:int,x2:int,x3:int,y1:int,y2:int,y3:int)->bool:
	pendiente1 = (y2-y1)/(x2-x1)
	pendiente2 = (y3-y2)/(x3-x2)
	if pendiente1 == pendiente2:
		return True
	else:
		return False
		

def son_colineales(x1:int,x2:int,x3:int,y1:int,y2:int,y3:int)->bool:
	pendiente1 = (y2-y1)/(x2-x1)
	pendiente2 = (y3-y2)/(x3-x2)
	
	return pendiente1 == pendiente2
		
	
x1=(int(input('ingrese numero x1: ')))
x2=(int(input('ingrese numero x2: ')))
x3=(int(input('ingrese numero x3: ')))
y1=(int(input('ingrese numero y1: ')))
y2=(int(input('ingrese numero y2: ')))
y3=(int(input('ingrese numero y3: ')))
print(son_colineales(x1,x2,x3,y1,y2,y3))	

'''

##################tercera actividad. Bogota-Tokio

def calcular_precio_pasaje(temporada_alta: bool, compañia: str, edad: int, estudiante: bool)->int:
	precio = 5000000
	variaciones =0
	seguro = False
	
	if compañia =='ALAS':
		if temporada_alta:
			variaciones +=0.3
		else:
			if edad >=18 and estudiante:
				variaciones -=.1
			
	elif compañia == 'VOLAR':
		if temporada_alta:
			variaciones +=0.2
		if edad > 60:
			seguro = True
			
	if edad<18:	
		variaciones -=0.5

	precio *=(1+variaciones)
	
	if seguro:
		precio +=100000
	
	return round(precio)

#PROGRAMA PRINCIPAL
temp=bool(input('Temporada alta? Escriba 1 si SI o 0 si NO: '))
compañia=str(input('Compania? Escriba ALAS o VOLAR: '))
edad=int(input('Indique su edad: '))
est=bool(input('Estudiante? Escriba 1 si SI o 0 si NO: '))

tarifa =calcular_precio_pasaje(temp, compañia, edad, est)
print('Su tarifa es: ',str(tarifa))
	
	
			


