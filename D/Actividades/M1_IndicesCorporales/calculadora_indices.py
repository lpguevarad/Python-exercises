########## Definicion de funciones Calculadora de indices corporales###############

def calcular_IMC(peso,altura):
	IMC = peso/(altura**2)
	return IMC
	
def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
	PGC = 1.2*calcular_IMC(peso, altura)+0.23*edad-5.4-valor_genero
	return PGC 

def calcular_calorias_reposo(peso, altura, edad, valor_genero):
	TMB = (10*peso)+(6.25*altura)-(5*edad)+valor_genero
	return TMB

def calcular_calorias_actividad(peso, altura, edad, valor_genero, valor_actividad):
	TMB_actividad_fisica = calcular_calorias_reposo(peso, altura, edad, valor_genero)*valor_actividad
	return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
	rango_inf = calcular_calorias_reposo(peso, altura, edad, valor_genero)*.8
	rango_sup = calcular_calorias_reposo(peso, altura, edad, valor_genero)*.85
	return rango_inf, rango_sup

#####funcion extra
def consumo_calorias_recomendado_para_adelgazar_act(peso, altura, edad, valor_genero,valor_actividad):
	rango_inf = calcular_calorias_actividad(peso, altura, edad, valor_genero,valor_actividad)*.8
	rango_sup = calcular_calorias_actividad(peso, altura, edad, valor_genero,valor_actividad)*.85
	return rango_inf, rango_sup
	


