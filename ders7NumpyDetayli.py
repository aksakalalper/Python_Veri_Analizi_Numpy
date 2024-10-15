import numpy as np
import matplotlib.pyplot as plt

a=np.array([1,2,3]) #tek boyutlu dizi
b=np.array([[1,2,3],[1,2,3]]) #2 boyutlu dizi
c=np.array([[[1,2,3],[11,22,33],[111,222,333]]]) #3 boyutlu dizi

print(a)
print(b)
print(c)

d=np.ones((3,3),dtype=int) 
print(d)

c=c.reshape(3,3) #matrise cevrildi.
print(c[0,1]) #0.satir 1.sutun getirildi.
print(c+d)

print(np.sin(np.pi/2))
str1="my name is"
str2="khkak"
print(np.char.add(str1,str2)) #iki ayri char dizisi toplandi.

