import numpy as np #numpy kutuphanesi import edildi

#python listesi
list1=[1,2,3,4,5,5,6,6,6]

#numpy dizisi
npArray=np.array([1,2,3,4,5,5,6,6,6])

print(type(npArray))

pyMulti=[[1,2,3],[4,4,4],[1,1,]] #cok boyutlu python dizisi.

npMulti=npArray.reshape(3,3) #matris olusturuldu.
print(pyMulti)
print(npMulti)

print(npArray.ndim) #dizi boyutu yazdirilir. 1x3 tek boyutlu dizi
print(npMulti.ndim) #2 boyutlu dizi 3x3 

print(npArray.shape) #
print(npMulti.shape) #sekilleri yazdirildi.

