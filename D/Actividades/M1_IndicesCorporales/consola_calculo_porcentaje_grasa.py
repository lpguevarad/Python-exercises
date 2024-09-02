import calculadora_indices as calc

def exe_calcular_IMC(peso,altura):
	IMC =calc.calcular_IMC(peso, altura)
	return IMC
	
def exe_calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
	PGC =calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
	print(round(PGC,2),'%')


def iniciar_app():
	peso = float(input('Ingresar peso (en kilogramos): '))
	altura = float(input('Ingresar altura (en metros): '))
	edad = float(input('Ingresar edad (en años): '))
	valor_genero = float(input('Ingresar el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: '))
	exe_calcular_IMC(peso,altura)
	exe_calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
	
iniciar_app()
