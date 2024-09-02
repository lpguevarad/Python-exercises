#########Interfaz con el usuario divisas Permitn datos entrada y salida################

import libreria_divisas as lb

def exe_convertir_a_dolares(trm):
	pesos = float(input('Ingresar valor en pesos: '))
	dolares = lb.convertir_a_dolares(pesos, trm)
	print(pesos, ' pesos equivalen a ',round(dolares,2),' dolares')

def exe_convertir_a_pesos(trm):
	dolares = float(input('Ingresar valor en dolares: '))
	pesos = lb.convertir_a_pesos(dolares, trm)
	print(dolares, ' dolares equivalen a ',round(pesos,2),' pesos')
	
def iniciar_app():
	trm = float(input('Ingresar valor de TRM: '))
	exe_convertir_a_dolares(trm)
	exe_convertir_a_pesos(trm)
	
iniciar_app()
