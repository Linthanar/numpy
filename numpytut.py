import numpy as np

a = np.array([[1,2,3],[3,2,1]], dtype='int16')

print(a)

# this is share
print('shape',np.shape(a))

# print dimmension
print('dimmension',a.ndim)

# size of the array
print('size',a.size)

# data type
print('data type',a.dtype)

# show how many bytes array has
print('size',a.itemsize)

# get total size
print('total size', a.size * a.itemsize)
print('total size',a.nbytes)


b = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]], dtype = 'int8')
print(b)
print('data type',b.dtype)

# accessing elements of array by [row,col]
print(b[1,2])

c = np.random.randint(1,7,size=(3,3))
print(c)

d = np.random.rand(1,1)
print(d)

# any

# where