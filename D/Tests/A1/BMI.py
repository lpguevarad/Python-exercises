def calcular_BMI(w,h):
	BMI = w/(h**2)
	return BMI
	
w_lb = input('Ingresar valor de peso: ')
h_lb = input('Ingresar valor de altura: ')

w_si=float(w_lb)*0.45
h_si=float(h_lb)*0.025

print('Su BMI con los datos dados, es: ',round(calcular_BMI(w_si,h_si),2))

