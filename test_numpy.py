
import numpy as np

# create an array

arr1 = np.array([1,2,3,4,5,6,7])
print(arr1)
arr2 = np.ones([3,4])
a=arr2.flatten()
print('flatten' ,a)
print(arr2)
print(arr2.shape)

rand_arr3 = np.random.randint(1,100,20).reshape(5,4)
print(rand_arr3)

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(np.mean(rand_arr3))
print(np.min(rand_arr3))
print(np.max(rand_arr3))

arr4 = np.random.rand()
print(arr4)
arr5 = np.random.randint(5)
print(arr5)
arr6 = np.random.randn()
print(arr6)

print('dot product', np.dot(array1,array2))


