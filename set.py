print('***** Restricting List Demo *****')
print('** Create a Tuple')
# Create a Tuple - this list cannot be changed by the program uses () instead of []. Values CAN be repeated
zoo = ('Kangaroo', 'Leopard','Moose')
print(' * Tuple: ',zoo,'\tLength',len(zoo))
print(' *',type(zoo))
print('** Create a Set')
# Create a Set - A regular list that cannot contain repeat values.  Uses {}
bag = {'Red','Green','Blue'}
print(' * Set: ',bag,'\tLength',len(bag))
print('** Add to Set')
bag.add('Yellow')
print(' * Set: ',bag,'\tLength',len(bag))
print(' *',type(bag))
print('\n** Find Values in a Set')
print(' * Green in bag set?:','Green' in bag)
print(' * Orange in bag set?:','Orange' in bag)
print('\n** Create New Set & Compare')
box = {'Red','Purple','Yellow'}
print(' * New Set: ',box,'\tLength',len(box))
# Return items that are in both sets
print(' * Common Values:',bag.intersection(box))
# Return values that are present in set1(bag) but not in set2(box)
print(' * Different Values in Set1  :',bag.difference(box))