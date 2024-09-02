def es_divisible(n:int,d:int)->int:
	if n%2*d==0:
		respuesta = 2
	elif n%d==0:
		respuesta = 1
	else:
		respuesta = 0
		
	return respuesta

n=5.5
d=1
print(es_divisible(n,d))
