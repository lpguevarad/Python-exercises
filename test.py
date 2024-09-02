'''
#lang = input('Idioma: ')
#lang = str()
def idioma(lang):

	if lang =='fr':
		return 'Bonyurt'
	elif lang =='en':
		return 'Hi'
	else:
		return 'Hola'

print(idioma('es'))





def computepay(hrs, rate):
	if hrs <= 40:
		return hrs*rate
	else:
		return 420+((hrs-40)*(rate*1.5))

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay", p)



while True:
	line = input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break 
	print(line)
print ('done')



NumMasgrande  = -1
print ('Primer',NumMasgrande)
for Numeros in [3,15,78,56,0]:

	if Numeros > NumMasgrande:
		NumMasgrande = Numeros
	print(NumMasgrande,Numeros)
print('Final',NumMasgrande)



zork = 0
print ('Primer',zork)
for cosa in [3,15,78,56,0]:
	zork = zork + cosa
	print (zork, cosa)
print ('Final',zork)
	


tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)	
'''
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')


