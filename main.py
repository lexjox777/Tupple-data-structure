#  Tupple items are enclosed in round brackets
# tuple=() 
# # Tuple is ordered
# tuple=('cat',[4,3,2,1], (1,2,3))
# tuple=1234, 4321
# tuple= 'hello',
# tuple= ('hello',)
# Tuple is immutable' can not be changed'
# tuple=(1,2,3,4)
# tuple[0]='5'
# print(tuple)

# Tuple elements do not need to be unique

# Tuple can be of different data types
# tuple=('cat',[4,3,2,1], (1,2,3))


#=======================
''' Acess Tuple Elements
'''

# tuple=(1234, 4321, 'hello')
# print(tuple[0])
# print(tuple[-2])


#=======================
'''
# Slicing Tuple
# '''
# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# print(fruits[:2])
# print(fruits[::2])
# print(fruits[:-2])
# print(fruits[2:])

# #==================
# '''
# Changing Tuple
# '''
# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# fruits[1]='lemon'
# print(fruits)
# # Tuple is immutable

# #================

# '''
# Deleting Tuple
# # '''
# # fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')

# # del fruits[0]
# # print(fruits)


'''
Tuple Methods
'''

# print(dir(list))
# print(dir(tuple))

fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')

print(fruits.count('orange'))
print(fruits.index('orange'))