"""
import  math

def vel_en_caida_libre(altura):
	vel_f= (2*g*altura)**0.5
	return vel_f
	

g = 9.8 #m/s**2
altura =input('Altura a la que lanza el objeto: ')
altura=float(altura)
print('La velocidad final es:',round(vel_en_caida_libre(altura),2))
"""

def f_1():
	return 'Hola mi amigo, '

def f_2(palabra):
	return f_1()+str(palabra)
	
resultado =print(f_2('Juan'))
print('Es: '+ str(resultado))

