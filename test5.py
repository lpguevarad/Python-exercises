#hrs = input("Enter Hours:")
#h = float(hrs)
#Tarifa=input('Ingrese tarifa:')
#Tarifa=float(Tarifa)



#if h <= 40:
#    below=h*Tarifa
#    print(below)
#else:
    #above=(40*Tarifa)+(1.5*Tarifa*(h-40))
    #print(above)
    
    
score = input("Enter Score: ")
f_score=float(score)


if f_score <0 or f_score >1:
	print('Error. Fuera de rango')
	
elif f_score >=0.9:
	print('A')
elif f_score >=0.8:
	print('B')
elif f_score >=0.7:
	print('C')
elif f_score >=0.6:
	print('D')
elif f_score <0.6:
	print('F')





