##################Primer version############
'''
numero = int(input('Digite un numero de 10 cifras: '))
conteo = {}


#1
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#2
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#3
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#4
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#5
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#6
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#7
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#8
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#9
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10

#10
digito = numero%10

if digito in conteo:
	conteo[digito] += 1
else:
	conteo[digito] = 1
numero = numero// 10


print(conteo)

##################Segunda version###############

def contar(num:int,diccionario:dict)->dict:

	digito = numero %10
	if digito in diccionario:
		diccionario[digito] += 1
	else:
		diccionario[digito] = 1
		
	return diccionario
	
#PROGRAMA PRINCIPAL#####

numero =int(input('Digite numero de 10 cifras: '))

conteo={}

#1
conteo =contar(numero, conteo)
numero = numero//10

#2
conteo =contar(numero, conteo)
numero = numero//10

#3
conteo =contar(numero, conteo)
numero = numero//10

#4
conteo =contar(numero, conteo)
numero = numero//10

#5
conteo =contar(numero, conteo)
numero = numero//10

#6
conteo =contar(numero, conteo)
numero = numero//10

#7
conteo =contar(numero, conteo)
numero = numero//10

#8
conteo =contar(numero, conteo)
numero = numero//10

#9
conteo =contar(numero, conteo)
numero = numero//10

#10
conteo =contar(numero, conteo)
numero = numero//10

print(conteo)



#######################Tercera version#######################	

def contar(num:int,diccionario:dict)->int:

	digito = numero %10
	if digito in diccionario:
		diccionario[digito] += 1
	else:
		diccionario[digito] = 1
		
	return num//10

numero =int(input('Digite numero de 10 cifras: '))	
conteo={}

numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)

print(conteo)
'''
################Cuarta version#####################

def contar(num:int,diccionario:dict)->int:

	digito = numero %10
	diccionario[digito] = diccionario.get(digito, 0) + 1
		
	return num//10
	
numero =int(input('Digite numero de 10 cifras: '))	
conteo={}

numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)
numero = contar(numero, conteo)

print(conteo)
