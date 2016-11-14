print('***** Associating List Demo *****')
''' Dictionary - data container that can store multiple items of data as a list of key:value pairs
    Unlike regular lists contain values, which are referred to by their index number [0], values stored
    in dictionaries are referenced by their associated key
'''
print('** Create a Dictionary')
dict={'name':'Bob','ref':'Python','sys':'Win'}
print(' * Display Dictionary:',dict)
print(' * Single Value:',dict['ref'])
print('\n** Display Keys')
print('Keys:',dict.keys())
print('\n** Delete & Replace')
del dict['name']
dict['user']= 'Tom'
print(' * New Dict:',dict)
print('\n** Search')
print(' * Is There a "name" Key?:','name' in dict)