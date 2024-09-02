def buscar_estudiante(est1:dict,est2:dict,est3:dict,est4:dict,nom:str)->str:
	buscado= None
	
	if est1 ['nombre'] == nom:
		buscado = est1
	elif est2 ['nombre'] == nom:
		buscado = est2
	elif est3 ['nombre'] == nom:
		buscado = est3
	elif est4 ['nombre'] == nom:
		buscado = est4

	return buscado
	
def est_riesgo(est1:dict,est2:dict,est3:dict,est4:dict):
	e_riesgo = {}

	if est1	['promedio'] <=3.4:
		e_riesgo[est1['codigo']] = est1['promedio']
	if est2	['promedio'] <=3.4:
		e_riesgo[est2['codigo']] = est2['promedio']
	if est3	['promedio'] <=3.4:
		e_riesgo[est3['codigo']] = est3['promedio']
	if est4	['promedio'] <=3.4:
		e_riesgo[est4['codigo']] = est4['promedio']
	
	return e_riesgo

def avanzar_sem(est1:dict,est2:dict,est3:dict,est4:dict)->None:
	
	est1 ['ssc'] += 1
	est2 ['ssc'] += 1
	est3 ['ssc'] += 1
	est4 ['ssc'] += 1	
	
	
e_1 = {'nombre':'Lina','codigo':'2021','genero':'femenino','carrera':'Sistemas','promedio':4.78,'ssc':2}

e_2 = {'nombre':'Laura','codigo':'2022','genero':'femenino','carrera':'Civil','promedio':3.21,'ssc':3}

e_3 = {'nombre':'Felipe','codigo':'2023','genero':'masculino','carrera':'Fisica','promedio':4.9,'ssc':1}

e_4 = {'nombre':'Carlos','codigo':'2024','genero':'masculino','carrera':'Economia','promedio':3.87,'ssc':6}	

nombre = input('Ingrese el nombre del estudiante a buscar: ')

est_buscado=buscar_estudiante(e_1,e_2,e_3,e_4,nombre)

if est_buscado is None:
	print('El estudiante no existe')
else:
	print('El estudiante existe y su codigo es: '+est_buscado['codigo'])

avanzar_sem(e_1,e_2,e_3,e_4)
riesgo = est_riesgo(e_1,e_2,e_3,e_4)

print('Estudiante 2 estara en semestre #: ',e_2['ssc'])	
print(riesgo)
