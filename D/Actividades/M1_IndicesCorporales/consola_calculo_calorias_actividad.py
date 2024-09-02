import calculadora_indices as calc

def exe_calcular_calorias_reposo(peso, altura, edad, valor_genero):
	TMB =calc.calcular_calorias_reposo(peso, altura, edad, valor_genero)
	return TMB
	
def exe_calcular_calorias_actividad(peso, altura, edad, valor_genero,valor_actividad):
	TMB_actividad_fisica =calc.calcular_calorias_actividad(peso, altura, edad, valor_genero, valor_actividad)
	print(round(TMB_actividad_fisica,2))


def iniciar_app():
	peso = float(input('Ingresar peso (en kilogramos): '))
	altura = float(input('Ingresar altura (en centimetros): '))
	edad = float(input('Ingresar edad (en años): '))
	valor_genero = float(input('Ingresar el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
	valor_actividad = float(input('Ingresar cualquiera de los siguientes valores segun actividad semanal: \n 1.2: Poco o ningun ejercicio. \n 1.375: Ejercicio ligero (1-3 días/semana). \n 1.55: Ejercicio moderado (3-5 días/semana). \n 1.725: Deportista  (6-7 días/semana). \n 1.9: Atleta (Entrenamientos mañana y tarde): '))
	exe_calcular_calorias_reposo(peso, altura, edad, valor_genero)
	exe_calcular_calorias_actividad(peso, altura, edad, valor_genero,valor_actividad)
	
iniciar_app()
