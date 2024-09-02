import calculadora_indices as calc

	
def exe_calcular_porcentaje_calorias_reposo(peso, altura, edad, valor_genero):
	TMB =calc.calcular_calorias_reposo(peso, altura, edad, valor_genero)
	print(round(TMB,2))


def iniciar_app():
	peso = float(input('Ingresar peso (en kilogramos): '))
	altura = float(input('Ingresar altura (en centimetros): '))
	edad = float(input('Ingresar edad (en años): '))
	valor_genero = float(input('Ingresar el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
	exe_calcular_porcentaje_calorias_reposo(peso, altura, edad, valor_genero)
	
iniciar_app()
