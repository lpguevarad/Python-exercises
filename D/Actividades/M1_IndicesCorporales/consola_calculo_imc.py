import calculadora_indices as calc

def exe_calcular_IMC(peso,altura):
	IMC =calc.calcular_IMC(peso, altura)
	print(round(IMC,2))


def iniciar_app():
	peso = float(input('Ingresar peso (en kilogramos): '))
	altura = float(input('Ingresar altura (en metros): '))
	exe_calcular_IMC(peso, altura)
	
iniciar_app()
