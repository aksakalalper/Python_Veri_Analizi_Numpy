import numpy as np

numbers=np.array([0,5,10,15,50,75])
result=numbers[5]
print(result)
numbers2=np.array([[1,2,3],[5,5,5],[7,6,5]])
print(numbers2[0]) #0.indeks geldi
print(numbers2[0,2]) #0.  indeksin 2. indeksi geldi.
print(numbers2[:,0]) #butun satirlarin 0. indeksleri geldi
print(numbers2[:,0:2]) #butun satirlarda 0 ve 2. indeksi getirdi.
print(numbers2[-1,:])

arr1=np.arange(0,10)
arr2=arr1
print(arr1)
print(arr2)

arr2[0]=5
print(arr2)
print(arr1)

arr2=arr1.copy()
arr1[1]=99
print(arr1)
print(arr2)
