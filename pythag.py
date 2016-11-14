# a^2 + b^2 = c^2
# Check if the value entered is a b or c
import math
# create Tuple
values = ('a','b','c')
print('------------------------------------')
print('Pythagoras Theorem')
print('a^2 + b^2 = c^2')
print('------------------------------------')
print(' |*')
print(' | *')
print('a|  *')
print(' |   * c')
print(' |__  *')
print(' |__|__*')
print('     b')
print('------------------------------------')
missing = input('Which side is unknown? (a,b,c):')
valid = missing in values
while valid == 0: #false
    print('** ERROR ** \nPlease choose a,b or c ONLY')
    missing = input('Which side is unknown? (a,b,c):')
    valid = missing in values

if missing == 'a':
    # a is unknown
    b = int(input('Enter Side b:'))
    c = int(input('Enter Side c:'))

    while c <= b:
        print('** ERROR ** \nc is less or equal to b')
        c = int(input('Enter Side c:'))

    a2 = (c ** 2) - (b ** 2)
    a = math.sqrt(a2)

elif missing == 'b':
    # b is unknown
    a = int(input('Enter Side a:'))
    c = int(input('Enter Side c:'))

    while c <= a:
        print('** ERROR ** \nc is less or equal to a')
        c = int(input('Enter Side c:'))

    b2 = (c**2)-(a**2)
    b = math.sqrt(b2)

elif missing == 'c':
    # c is unknown
    a = int(input('Enter Side a:'))
    b = int(input('Enter Side b:'))
    c2 = int((a ** 2) + (b ** 2))
    c = math.sqrt(c2)

# Print side values (round to 2dp)
print('------------------------------------')
print('Side a =', float(round(a,2)))
print('Side b =', float(round(b,2)))
print('Side c =', float(round(c,2)))
print('Area:',round((a*b)/2,2))
print('------------------------------------')
print('END')