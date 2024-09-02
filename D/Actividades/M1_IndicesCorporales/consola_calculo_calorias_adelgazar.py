import calculadora_indices as calc

def exe_calcular_calorias_reposo(peso, altura, edad, valor_genero):
	TMB =calc.calcular_calorias_reposo(peso, altura, edad, valor_genero)
	return TMB
	
def exe_calcular_calorias_actividad(peso, altura, edad, valor_genero,valor_actividad):
	TMB_actividad_fisica =calc.calcular_calorias_actividad(peso, altura, edad, valor_genero, valor_actividad)
	return TMB_actividad_fisica
	
#######basado en el TMB sin actividad fisica
def exe_consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero): 
	calorias_adelgazar=calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
	val_inf=calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)[0]
	val_sup=calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)[1]
	print('En reposo para adelgazar es recomendado que consumas entre:',round(val_inf,2),'y',round(val_sup,2),'calorías al día')
	
#######basado en el TMB con actividad fisica
def exe_consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero, valor_actividad): 
	calorias_adelgazar=calc.consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero,valor_actividad)
	val_inf=calc.consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero,valor_actividad)[0]
	val_sup=calc.consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero,valor_actividad)[1]
	print('Si haces actividad física, para adelgazar es recomendado que consumas entre:',round(val_inf,2),'y',round(val_sup,2),'calorías al día')
	
def iniciar_app():
	peso = float(input('Ingresar peso (en kilogramos): '))
	altura = float(input('Ingresar altura (en centimetros): '))
	edad = float(input('Ingresar edad (en años): '))
	valor_genero = float(input('Ingresar el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
	valor_actividad = float(input('Ingresar cualquiera de los siguientes valores segun actividad fisica semanal: \n 1.2: Poco o ningun ejercicio. \n 1.375: Ejercicio ligero (1-3 días/semana). \n 1.55: Ejercicio moderado (3-5 días/semana). \n 1.725: Deportista  (6-7 días/semana). \n 1.9: Atleta (Entrenamientos mañana y tarde): '))
	
	exe_calcular_calorias_reposo(peso, altura, edad, valor_genero)
	exe_consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
	exe_consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero,valor_actividad)
	
iniciar_app()
