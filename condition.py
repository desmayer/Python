a=1
value = input('Enter a Number:')

while value != int:
	print('\nNot A Number')
	value = input('Enter a number:')

b=int(input)

''' \n NEW LINE 	'''
''' 'One' [TRUE] if (var == 1) else [FALSE] 'Not One'	'''

print('\nVariable a is :','One' if ( a== 1) else 'Not One')
print('Variable a is :','Even' if ( a % 2 == 0) else 'Odd')

print('\nVariable b is :','One' if ( b== 1) else 'Not One')
print('Variable b is :','Even' if ( b % 2 == 0) else 'Odd')

max = a if (a>b) else b

print('\nGreater Value Is:',max)
print('\nFirst Number:',a)
print('Second Number:',b)
print('\n',a,'x',b,'=',a*b)