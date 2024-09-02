'''
num = input("Numero del 0 al 9: ")
num = int(num)
if num>10:
	if num<5:
		print ("menor que cinco")
	elif num >=5:
		print ("cinco o mas")
print ("Error")
'''

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
