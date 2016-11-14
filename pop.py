basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print('***** List Demo *****')
print('** Show Items in Basket & Count')
print(' * Basket List:', basket)
# len() will print the number of items in the list
print(' * Number of Items in Basket', len(basket))
print('** Add New Items in Basket & Remove')
basket.append('Damson')
print(' * Updated Basket:',basket)
print(' * Remove Last Item:',basket.pop())
print(' * New Basket:',basket)
print('** Add Crate to Basket')
basket.extend(crate)
print(' * Extended: ',basket)
print('** Remove 2nd Item')
print(' * Item to Remove:', basket[1])
# a list starts at [0]. [1] is the second item.  Future demo could involve user entering a number to remove a certain item?
del basket[1]
print(' * Item Removed:',basket)
print(' ** Remove Slice from List')
print(' * Items to Remove:',basket[1:3])
# [x:y] x is the start value and y is the value to stop at - does not remove this value.  In this case the items in list positions 1 & 2 are removed
del basket[1:3]
print(' * Items Removed:',basket)
print('***** List Demo *****')
print('***** Finished 14/11/16 *****')